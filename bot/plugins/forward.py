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
from .dbs.dump_db import get_dump


@user.on(events.NewMessage(outgoing=True, pattern="\\.fwd"))
async def _(e):
    if e.reply_to:
        reply = await e.get_reply_message()
        await user.forward_messages(int(get_dump()), reply)
        await e.edit("`Successfully Forwarded`")
        return
    await e.edit("`reply to any media , document and others.`")


@bot.on(events.NewMessage(pattern="\\/fwd"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    if e.reply_to:
        reply = await e.get_reply_message()
        await bot.forward_messages(int(get_dump()), reply)
        await e.edit("`Successfully Forwarded`")
        return
    await e.edit("`reply to any media , document and others.`")
