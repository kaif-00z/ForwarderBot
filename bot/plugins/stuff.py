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
from .dbs.boardcast_db import add_user

PUBLIC_H_MENU = (
    "__Help menu for user__\n\n"
    + "• `/start` - **will start the bot**\n"
    + "• `/ping` - **Will show the connection speed**\n"
    + "• `/help` - **Will Open this**\n"
    + "• `/search <query>` - **Will send all files/message/media related to the query to bot user from storage channel**\n\n"
    + "• `/telegraph <reply to media>` - **Will upload it in telegra.ph**\n"
)

HELP_MENU = (
    "__Help menu for Authorised User__\n\n"
    + "• `/help` - **Will open this menu**\n"
    + "• `/boardcast` - **Will Boardcast a message to all bot users nd groups**\n"
    + "• `/fwd` - **Reply to any file/media/message to Forward the message to Dump channel**\n"
    + "• `/setredis <key> <value>` - **Will SET with given key and value in the database**\n"
    + "• `/getredis <key>` - **Will GET value of given key from the database**\n"
    + "• `/delredis <key>` - **Will DELETE the given key from the database**\n"
    + "• `/allkeys` - **Will give list of all KEYS in your Database**\n"
    + "• `/telegraph <reply to media>` - **Will upload it in telegra.ph**\n"
    + "• `/listauth` - **Will list all the Authorized User**\n"
    + "• `/listbanuser` - **Will list all the Banned User**\n\n"
    + "__Help menu for user__\n\n"
    + "• `/start` - **will start the bot**\n"
    + "• `/ping` - **Will show the connection speed**\n"
    + "• `/help` - **Will tell user to use /search <query>**\n"
    + "• `/search <query>` - **Will send all files/message/media related to the query to bot user from storage channel**\n\n"
    + "• `/telegraph <reply to media>` - **Will upload it in telegra.ph**\n"
    + "__Help menu for UserBot__\n\n"
    + "• `.ping` - **Will show the connection speed**\n"
    + "• `.telegraph <reply to media>` - **As said above**\n"
    + "• `.fwd` - **as said above**\n"
    + "• `.allkeys` - **as said above**\n"
    + "• `.setredis <key> <value>` - **as said above**\n"
    + "• `.getredis <key>` - **as said above**\n"
    + "• `.delredis <key>`- **as said above**\n"
    + "• `.eval <script>` - **Evaluate script (python3)**\n"
    + "• `.bash <cmd>` - **bash = bash, simple 😁**\n\n"
    + "__Owner Restricted Command__\n\n"
    + "• `/auth <id/reply>` - **Will Authorised that user**\n"
    + "• `/remauth <id/reply>` - **Will Unauthorised that user**\n"
    + "• `/ban <id/reply>` - **Will ban the user**\n"
    + "• `/unban <id/reply>` - **Will unban the user**\n"
)


@bot.on(events.NewMessage(incoming=True, pattern="\\/ping"))
async def _(event):
    if is_ban(event.sender_id):
        return await event.reply(
            "You are Banned contact the Admin of the Bot for Unban"
        )
    t = time.time()
    now = dt.now()
    x = await event.reply("`Pɪɴɢ!!!`")
    tt = time.time() - t
    v = ts(int((now - uptime).seconds) * 1000)
    p = float(str(tt)) * 1000
    await x.edit(f"**Uptime**: {v}\n**Pɪɴɢ !!**: {int(p)}ms")


@user.on(events.NewMessage(outgoing=True, pattern="\\.ping"))
async def _(event):
    t = time.time()
    now = dt.now()
    x = await event.edit("`Pɪɴɢ!!!`")
    tt = time.time() - t
    v = ts(int((now - uptime).seconds) * 1000)
    p = float(str(tt)) * 1000
    await x.edit(f"**Uptime**: {v}\n**Pɪɴɢ !!**: {int(p)}ms")


@bot.on(events.NewMessage(incoming=True, pattern="\\/start"))
async def strt(event):
    if is_ban(event.sender_id):
        add_user(event.chat_id)
        return await event.reply(
            "You are Banned contact the Admin of the Bot for Unban"
        )
    add_user(event.chat_id)
    await event.reply(
        f"Hi `{event.sender.first_name}` \n**Hi I am file forwarder bot or a searcher bot ! , for more send** /help",
        buttons=[
            [
                Button.url(
                    "Repository", url="https://github.com/kaif-00z/ForwarderBot"
                ),
                Button.url("DEVELOPER", url="t.me/kaif_00z"),
            ],
        ],
    )


@bot.on(events.NewMessage(incoming=True, pattern="\\/help"))
async def hlp(event):
    if not (is_auth(event.sender_id)):
        if is_ban(event.sender_id):
            return await event.reply(
                "You are Banned contact the Admin of the Bot for Unban"
            )
        await event.reply(PUBLIC_H_MENU)
    else:
        await event.reply(HELP_MENU)


@user.on(events.NewMessage(outgoing=True, pattern="\\.help"))
async def _(event):
    await event.edit(HELP_MENU)
