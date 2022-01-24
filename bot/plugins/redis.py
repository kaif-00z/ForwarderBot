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


@bot.on(events.NewMessage(incoming=True, pattern="^/allkeys$"))
async def keys(event):
    if not (is_auth(event.sender_id)):
        return
    msg = "**All Keys in your Redis Database**\n\n"
    for key in sorted(dB.keys()):
        msg += f"• `{key}`\n"
    await event.reply(msg)


@bot.on(events.NewMessage(incoming=True, pattern="\\/setredis"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    key = e.text.split()[1]
    value = e.text.split()[2]
    if not key and value:
        return await e.reply("plz give key and value to set")
    try:
        dB.set(str(key), str(value))
        await e.reply(
            f"**Redis Key Value Pair Updated**\n**Key** : `{key}`\n**Value** : `{value}`"
        )
    except Exception as erc:
        LOGS.info(str(erc))
        await e.reply("something want wrong")


@bot.on(events.NewMessage(incoming=True, pattern="\\/getredis"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    key = e.text.split()[1]
    if not key:
        return await e.reply("Plz give a key to find its value")
    try:
        value = dB.get(str(key))
        if value:
            return await e.reply(f"**Key** : `{key}`\n**Value** : `{str(value)}`")
        return await e.reply("Key not Found")
    except Exception as rre:
        LOGS.info(str(rre))
        await e.reply("something went wrong")


@bot.on(events.NewMessage(incoming=True, pattern="\\/delredis"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    key = e.text.split()[1]
    if not key:
        return await e.reply("Plz give a key to delete it")
    try:
        x = dB.delete(str(key))
        if x == 1:
            return await e.reply(f"**Successfully Deleted {key}**")
        else:
            return await e.reply(f"**Key not Found**")
    except Exception as ror:
        LOGS.info(str(ror))
        await e.reply("Something Went Wrong")


@user.on(events.NewMessage(outgoing=True, pattern="\\.allkeys"))
async def _(event):
    message = "**All Keys in your Redis Database**\n\n"
    for key in sorted(dB.keys()):
        message += f"• `{key}`\n"
    await event.edit(message)


@user.on(events.NewMessage(outgoing=True, pattern="\\.getredis"))
async def _(e):
    key = e.text.split()[1]
    if not key:
        return await e.ediy("Plz give a key to find its value")
    try:
        value = dB.get(str(key))
        if value:
            return await e.edit(f"**Key** : `{key}`\n**Value** : `{str(value)}`")
        return await e.edit("Key not Found")
    except Exception as rre:
        LOGS.info(str(rre))
        await e.edit("something went wrong")


@user.on(events.NewMessage(outgoing=True, pattern="\\.delredis"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    key = e.text.split()[1]
    if not key:
        return await e.edit("Plz give a key to delete it")
    try:
        x = dB.delete(str(key))
        if x == 1:
            return await e.edit(f"**Successfully Deleted {key}**")
        else:
            return await e.edit(f"**Key not Found**")
    except Exception as ror:
        LOGS.info(str(ror))
        await e.edit("Something Went Wrong")
