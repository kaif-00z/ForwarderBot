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
from .dbs.dump_db import *


@user.on(events.NewMessage(outgoing=True, pattern="\\.webdump"))
async def _(event):
    cap = ""
    link = event.text.split()[1]
    fname = f"downloads/{event.text.split()[2]}"
    try:
        cap = event.text.split(" ", maxsplit=3)[3]
    except BaseException:
        pass
    ttt = time.time()
    try:
        x = await event.edit("`Downloading and Posting`")
        # await fast_download(x, link, fname)
        # await link_download(link, fname)
        success, error = await bash(f"wget {link} -O {fname}")
        if error:
            return LOGS.info(str(error))
        with open(fname, "rb") as s:
            ok = await upload_file(
                client=user,
                file=s,
                name=fname,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "uploading..")
                ),
            )
        if cap.strip():
            pass
        else:
            cap = fname.split("/")[1]
        await user.send_file(
            int(get_dump()),
            ok,
            force_document=True,
            thumb="thumb.jpg" or "",
            caption=f"`{cap}`",
        )
        await x.edit("`Successfully Posted`")
    except Exception as eror:
        LOGS.info(str(eror))


@bot.on(events.NewMessage(outgoing=True, pattern="\\/webdump"))
async def _(event):
    if not (is_auth(event.sender_id)):
        return
    cap = ""
    link = event.text.split()[1]
    fname = f"downloads/{event.text.split()[2]}"
    try:
        cap = event.text.split(" ", maxsplit=3)[3]
    except BaseException:
        pass
    ttt = time.time()
    try:
        x = await event.reply("`Downloading and Posting`")
        # await fast_download(x, link, fname)
        # await link_download(link, fname)
        success, error = await bash(f"wget {link} -O {fname}")
        if error:
            return LOGS.info(str(error))
        with open(fname, "rb") as s:
            ok = await upload_file(
                client=bot,
                file=s,
                name=fname,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "uploading..")
                ),
            )
        if cap.strip():
            pass
        else:
            cap = fname.split("/")[1]
        await bot.send_file(
            int(get_dump()),
            ok,
            force_document=True,
            thumb="thumb.jpg" or "",
            caption=f"`{cap}`",
        )
        await x.edit("`Successfully Posted`")
    except Exception as err:
        LOGS.info(str(err))
