#    This file is part of the Forwarder distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/ForwarderBot/blob/main/License> .


from . import *
from .dbs.ban_db import is_ban
from .dbs.req_db import get_req, get_req_channel


@bot.on(events.NewMessage(pattern="\\/request", func=lambda e: not e.is_private))
async def req(e):
    if is_ban(e.sender_id):
        return await event.reply(
            "You are Banned contact the Admin of the Bot for Unban"
        )
    if not (get_req()):
        return await e.reply("Request Function is Disabled")
    req = e.text.split(" ", maxsplit=1)[1]
    name = await name_get(e.sender_id, e.sender)
    msg_link = e.message.message_link
    button = [
        [
            Button.url("VIEW MESSAGE", msg_link),
            Button.inline("DELETE MESSAGE", data="delmsg"),
        ],
    ]
    x = await bot.send_message(
        int(get_req_channel()),
        f"<b>Request By {name}</b>\n<b>Request</b>: `{req}`",
        buttons=button,
        parse_mode="HTML",
    )
    msg_e_link = x.message_link
    btn = [[Button.url("VIEW MESSAGE", msg_e_link)]]
    await e.reply("Request is sent successfully", buttons=btn)


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("delmsg")))
async def _(e):
    if not (is_auth(e.sender_id)):
        return e.answer(
            "Only Admin Can Delete this Message, hurr!", cache_time=0, alert=True
        )
    o = await name_get(e.sender_id, e.sender)
    await e.delete()
    await bot.send_message(
        Var.LOG_CHANNEL, f"A Request Message Deleted By {o}", parse_mode="HTML"
    )
