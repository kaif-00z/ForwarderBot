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


import asyncio
import os
import re

from telethon import Button, events
from telethon.utils import get_display_name, pack_bot_file_id

from bot import *
from bot.config import Var
from bot.FastTelethon import download_file, upload_file
from bot.func import *

from .dbs.auth import *

# some function


async def logging(event, message):
    LOGS.info("sending logs in log channel..")
    await bot.send_message(Var.LOG_CHANNEL, message)


async def deep_logging(event, message):
    await bot.send_message(Var.LOG_CHANNEL, message)
    LOGS.info(str(message))


async def name_get(id, sender):
    uuname = get_display_name(sender)
    xxx = "<a href='tg://user?id={}'>{}</a>".format(id, uuname)
    return xxx


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err
