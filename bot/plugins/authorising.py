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


@bot.on(events.NewMessage(incoming=True, pattern="\\/auth (.*)"))
async def _(e):
    if e.sender_id != Var.OWNER_ID:
        return
    if e.reply_to:
        reply = await e.get_reply_message()
        user_id = reply.sender_id
        add_auth(int(user_id))
        await e.reply(f"{user_id} is now a authorised user")
        return
    user_id = e.pattern_match.group(1)
    if user_id.isdigit():
        add_auth(int(user_id))
    else:
        try:
            user = await bot.get_entity(id)
        except BaseException:
            return await e.reply("User Not Found")
        add_auth(user.id)
    await e.reply(f"{user_id} is now a authorised user")


@bot.on(events.NewMessage(incoming=True, pattern="\\/remauth (.*)"))
async def _(e):
    if e.sender_id != Var.OWNER_ID:
        return
    if e.reply_to:
        reply = await e.get_reply_message()
        user_id = reply.sender_id
        rem_auth(int(user_id))
        await e.reply(f"{user_id} is now unauthorised user")
        return
    user_id = e.pattern_match.group(1)
    if user_id.isdigit():
        rem_auth(int(user_id))
    else:
        try:
            user = await bot.get_entity(id)
        except BaseException:
            return await e.reply("User Not Found")
        rem_auth(user.id)
    await e.reply(f"{user_id} is now unauthorised user")


@bot.on(events.NewMessage(incoming=True, pattern="\\/listauth$"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    users = get_auth()
    txt = "Authorised users:\n\n"
    for id in users:
        try:
            o = await bot.get_entity(id)
        except BaseException:
            o = None
        if o:
            if o.username:
                txt += f"@{o.username} ({o.id})\n"
            else:
                txt += f"@{o.first_name} ({o.id})\n"
        else:
            txt += f"Unknown ({id})\n"
    await e.reply(txt)
