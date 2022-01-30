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

HELP_MENU = (
    "__Help menu for Authorised User__\n\n"
    + "• `/help` - **Will open this menu**\n"
    + "• `/boardcast` - **Will Boardcast a message to all bot users nd groups**\n"
    + "• `/dl <filename>` - **Reply to a file with /dl , filename is optional**\n"
    + "• `/ul <path of file>` - **Send the path of file given by bot when you do /dl**\n"
    + "• `/dump <filename> <caption>` - **It will Dump the file in DUMP_CHANNEL(default dump_channel==stroage_channel), filename and caption both are optional**\n"
    + "• `/fwd` - **Reply to any file/media/message to Forward the message to Dump channel**\n"
    + "• `/setredis <key> <value>` - **Will SET with given key and value in the database**\n"
    + "• `/getredis <key>` - **Will GET value of given key from the database**\n"
    + "• `/delredis <key>` - **Will DELETE the given key from the database**\n"
    + "• `/allkeys` - **Will give list of all KEYS in your Database**\n"
    + "• `/setthumb <telegraph link>` - **Will set Thumbnail**\n"
    + "• `/telegraph <reply to media>` - **Will upload it in telegra.ph**\n"
    + "• `/webdump <link> <filename> <caption>` - **It will download the file from link and dump it in DUMP_CHANNEL, filename required**\n"
    + "• `/linkdl <link>` - **Will Download from direct link**\n"
    + "• `/listauth` - **Will list all the Authorized User**\n"
    + "• `/listbanuser` - **Will list all the Banned User**\n\n"
    + "__Help menu for user__\n\n"
    + "• `/start` - **will start the bot**\n"
    + "• `/ping` - **Will show the connection speed**\n"
    + "• `/request <text>` - **Will send the request into REQUEST_CHANNEL(default log_channel)**\n"
    + "• `/help` - **Will tell user to use /search <query>**\n"
    + "• `/search <query>` - **Will send all files/message/media related to the query to bot user from storage channel**\n\n"
    + "__Help menu for UserBot__\n\n"
    + "• `.ping` - **Will show the connection speed**\n"
    + "• `.dl <filename>` - **as said above**\n"
    + "• `.ul <path of file>` - **as said above**\n"
    + "• `.dump <filename> <caption>` - **as said above**\n"
    + "• `.webdump <link> <filename> <caption>` - **as said above**\n"
    + "• `.linkdl <link>` - **As said above**\n"
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

MORE_HELP = (
    "**How to set DUMP_CHANNEL**\n"
    + "`.setredis DUMP_CHANNEL <id>` - Default is Storage Channel\n"
    "**How to Turn OFF and ON request function**\n"
    + "`.setredis REQUEST True` - To trun on Request Function\n"
    + "`.setredis REQUEST False` - To turn off Request Function\n"
    + "**How to Set REQUEST_CHANNEL**\n"
    + "`.setredis REQUEST_CHANNEL <id>` - Default is Log Channel\n"
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
        f"Hi `{event.sender.first_name}` \nFirst send /help",
        buttons=[
            [
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
        await event.reply(f"How to use, send `/search <query>` and see magic 😁")
    else:
        await event.reply(HELP_MENU, buttons=[[Button.inline("MORE", data="mm")]])


@user.on(events.NewMessage(outgoing=True, pattern="\\.help"))
async def _(event):
    await event.reply(HELP_MENU)
    await event.reply(f"__More Help__\n\n{MORE_HELP}")


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("mm")))
async def _(e):
    await e.edit(MORE_HELP)
