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


import os

import heroku3


async def heroku_dynos(event, appname, dynoss, dynotype):
    if appname and HEROKU_API and dynoss and dynotype:
        try:
            Heroku = heroku3.from_key(HEROKU_API)
            app = Heroku.apps()[appname]
            x = await event.edit("`processing...`")
            if dynoss == off:
                app.process_formation()[dynotype].scale(0)
                await x.edit("Successfully Dynos are turned off")
                return
            elif dynoss == on:
                app.process_formation()[dynotype].scale(1)
                await x.edit("Successfully Dynos are turned on")
                return
        except Exception as e:
            await deep_logging(str(e))
    else:
        await event.edit("App name, dynos and dynotype set is not found")
        exit(1)


async def heroku_logs(event, appname):
    x = await event.edit("`Processing...`")
    if not (HEROKU_API and appname):
        await x.edit("Please give appname and not forget to set Var.HEROKU_API")
        return
    try:
        app = (heroku3.from_key(HEROKU_API)).app(appname)
    except Exception as eror:
        await deep_logging(str(eror))
    await x.edit("`Downloading and Sending Logs...`")
    heroku_log = app.get_log()
    with open("heroku.log", "w") as log:
        log.write(heroku_log)
    await event.client.send_file(event.chat_id, file="heroku.log", thumb="", caption="")
    os.remove("heroku.log")
    await x.delete()


async def heroku_restart(event, appname):
    x = await event.edit("`processing...`")
    if not (HEROKU_API and appname):
        await x.edit("Please give appname and not forget to set Var.HEROKU_API")
        return
    try:
        app = (heroku3.from_key(HEROKU_API)).app(appname)
    except Exception as e:
        await deep_logging(str(e))
    app.restart()
    x.edit("Successfully restarted the app")
