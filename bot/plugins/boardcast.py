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
from .dbs.boardcast_db import *


@bot.on(events.ChatAction)
async def _(e):
    if e.user_added:
        if e.user and e.user.is_self:
            add_user(e.chat_id)
    elif e.left or e.kicked:
        if e.user and e.user.is_self:
            rem_user(e.chat_id)


@bot.on(events.NewMessage(incoming=True, pattern="\\/boardcast"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    users = get_users()
    await e.reply("Please use his feature Responsibly⚠️")
    await e.reply(
        f"Send a single Message To Broadcast😉`\n``\n`There are {len(users)} users currently using me👉🏻.\n\nSend /cancel to Cancel Process."
    )
    async with e.client.conversation(e.sender_id) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=e.sender_id))
        repl = await reply
        await e.delete()
        if repl.text and repl.text.startswith("/cancel"):
            return await repl.reply("Broadcast cancel")
    sent = await repl.reply("Broadcasting msg...")
    done, er = 0, 0
    for user in users:
        try:
            if repl.poll:
                await repl.forward_to(user)
            else:
                await bot.send_message(user, repl.message)
            await asyncio.sleep(0.2)
            done += 1
        except BaseException as ex:
            er += 1
            LOGS.info(str(ex))
    await sent.edit(f"Broadcast Completed To {done} users\n[Error in {er} users]")
    await bot.send_message(
        Var.LOG_CHANNEL,
        "{} **Broadcast a message**".format(await name_get(e.sender_id, e.sender)),
    )
