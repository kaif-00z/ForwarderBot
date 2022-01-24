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


from glob import glob
from importlib import import_module

from . import *

LOGS.info("• Loading Plugins & Starting •")

try:
    bot.start(bot_token=Var.BOT_TOKEN)
    user.start()
except Exception as exc:
    LOGS.info(str(exc))

plugins = glob("bot/plugins/*py")
for plugin in plugins:
    try:
        plugin = plugin.replace(".py", "").replace("/", ".")
        import_module(plugin)
        LOGS.info("• Successfully loaded all plugins")
    except Exception as er:
        LOGS.info(str(er))


LOGS.info("Bot has started...")
bot.loop.run_until_complete(startup())
bot.run_until_disconnected()
