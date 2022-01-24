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
from .dbs.ban_db import *


@bot.on(events.NewMessage(incoming=True, pattern="\\/ban (.*)"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    if e.reply_to:
        reply = await e.get_reply_message()
        user_id = reply.sender_id
        if (is_auth(user_id)) and e.sender_id == Var.OWNER_ID:
            ban(int(user_id))
        else:
            ban(int(user_id))
        await e.reply(f"successfully banned {user_id}")
        return
    user_id = e.pattern_match.group(1)
    if user_id.isdigit():
        if (is_auth(user_id)) and e.sender_id == Var.OWNER_ID:
            ban(int(user_id))
        else:
            ban(int(user_id))
    else:
        try:
            user = await bot.get_entity(id)
        except BaseException:
            return await e.reply("User Not Found")
        ban(user.id)
    await e.reply(f"successfully banned user {user_id}")


@bot.on(events.NewMessage(incoming=True, pattern="\\/unban (.*)"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    if e.reply_to:
        reply = await e.get_reply_message()
        user_id = reply.sender_id
        unban(int(user_id))
        await e.reply(f"successfully unbanned {user_id}")
        return
    user_id = e.pattern_match.group(1)
    if user_id.isdigit():
        unban(int(user_id))
    else:
        try:
            user = await bot.get_entity(id)
        except BaseException:
            return await e.reply("User Not Found")
        unban(user.id)
    await e.reply(f"successfully unbanned user {user_id}")


@bot.on(events.NewMessage(incoming=True, pattern="\\/listbanuser$"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    users = get_ban_user()
    txt = "Banned users:\n\n"
    for id in users:
        try:
            o = await bot.get_entity(id)
        except BaseException:
            o = None
        if u:
            if o.username:
                txt += f"@{o.username} ({o.id})\n"
            else:
                txt += f"@{o.first_name} ({o.id})\n"
        else:
            txt += f"Unknown ({id})\n"
    await e.reply(txt)
