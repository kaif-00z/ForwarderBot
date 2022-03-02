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
from .dba.link_db import is_link, get_link

Z = []
X = []


@bot.on(
    events.NewMessage(incoming=True, pattern="\\/search", func=lambda e: e.is_private)
)
async def search(event):
    if is_ban(event.sender_id):
        return await event.reply(
            "You are Banned contact the Admin of the Bot for Unban"
        )
    query = event.text.split(" ", maxsplit=1)[1]
    btn = [Button.inline("CANCEL PROCESS", data="cnc")]
    x = await event.reply("`searching...`", buttons=btn)
    async for message in user.iter_messages(Var.GROUP_ID, search=query):
        if message:
            if event.sender_id not in X:
                X.append(event.sender_id)
            msg = await bot.get_messages(Var.GROUP_ID, ids=message.id)
            await bot.send_message(event.chat_id, msg)
            if event.sender_id in Z:
                Z.remove(event.sender_id)
                return await x.delete()
            await asyncio.sleep(1)
            continue
    if event.sender_id not in X:
        await bot.send_message(
            event.chat_id,
            f"Nothing Found Related To Keyword : `{query}`",
        )
    else:
        await bot.send_message(
            event.chat_id,
            f"All Files Related To Keyword : `{query}` sent successfully.",
        )
        X.remove(event.sender_id)
    await x.delete()


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("cnc")))
async def _(event):
    Z.append(event.sender_id)


@bot.on(events.NewMessage(incoming=True, pattern="\\/link"))
async def _(event):
    if not is_link():
        return
    query = event.text.split(" ", maxsplit=1)[1].replace(" ","+")
    base = get_link()
    await event.reply(f"Get it [link]({base}search?q={query})")
