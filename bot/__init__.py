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


import sys
from logging import INFO, basicConfig, getLogger

from redis import Redis
from telethon import TelegramClient
from telethon.sessions import StringSession

from .config import Var

basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger(__name__)


try:
    redis_info = Var.REDIS_URI.split(":")
    dB = Redis(
        host=redis_info[0],
        port=redis_info[1],
        password=Var.REDIS_PASS,
        charset="utf-8",
        decode_responses=True,
    )
    LOGS.info("successfully connected to redis database")
except Exception:
    sys.exit(Exception)
    LOGS.info(str(Exception))

try:
    user = TelegramClient(StringSession(Var.SESSION), Var.API_ID, Var.API_HASH)
    bot = TelegramClient(None, Var.API_ID, Var.API_HASH)
    LOGS.info("successfully connected to telegram")
except Exception as e:
    LOGS.info("Environment vars are missing")
    LOGS.info(str(e))
    exit()


async def startup():
    mg = f"Bot is Botted Successfully"
    msg = f"🤖 Successfully Deployed Your Bot 🤖\nFor More Help- `.help`"
    await bot.send_message(Var.LOG_CHANNEL, msg)
    await bot.send_message(Var.LOG_CHANNEL, mg)
