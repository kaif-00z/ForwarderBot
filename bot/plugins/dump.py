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


# -----------------UserBot----------------------
@user.on(events.NewMessage(outgoing=True, pattern="\\.dump"))
async def dump(e):
    cap = ""
    fname = ""
    try:
        cap = e.text.split(" ", maxsplit=2)[2]
        fname = f"downloads/{e.text.split()[1]}"
    except BaseException:
        pass
    if e.reply_to:
        x = await e.edit("`Downloading...`")
        ttt = time.time()
        reply = await e.get_reply_message()
        filename = f"downloads/{reply.file.name}"
        file = reply.document
        with open(filename, "wb") as f:
            ok = await download_file(
                client=user,
                location=file,
                out=f,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "Downloading...")
                ),
            )
        if not fname:
            fname = filename
        else:
            os.rename(filename, fname)
        with open(fname, "rb") as s:
            oo = await upload_file(
                client=user,
                file=s,
                name=fname,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "uploading...")
                ),
            )
        if cap.strip():
            pass
        else:
            cap = fname.split("/")[1]
        if os.path.isfile("thumb.jpg"):
            await user.send_file(
                int(get_dump()),
                oo,
                force_document=True,
                thumb="thumb.jpg",
                caption=f"`{cap}`",
            )
        else:
            await user.send_file(
                int(get_dump()), oo, force_document=True, caption=f"`{cap}`"
            )
        await x.edit("`Successfully Posted`")
        return
    await e.edit("`reply to any media , document and others.`")


# --------------------Assistant-------------------------------


@bot.on(events.NewMessage(pattern="\\/dump"))
async def botdump(e):
    if not (is_auth(e.sender_id)):
        return
    cap = ""
    fname = ""
    try:
        fname = f"downloads/{e.text.split()[1]}"
        cap = e.text.split(" ", maxsplit=2)[2]
    except BaseException:
        pass
    if e.reply_to:
        x = await e.reply("`Downloading...`")
        ttt = time.time()
        reply = await e.get_reply_message()
        filename = f"downloads/{reply.file.name}"
        file = reply.document
        with open(filename, "wb") as f:
            ok = await download_file(
                client=bot,
                location=file,
                out=f,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "Downloading...")
                ),
            )
        if not fname:
            fname = filename
        else:
            os.rename(filename, fname)
        with open(fname, "rb") as s:
            oo = await upload_file(
                client=bot,
                file=s,
                name=fname,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "uploading...")
                ),
            )
        if cap.strip():
            pass
        else:
            cap = fname.split("/")[1]
        if os.path.isfile("thumb.jpg"):
            await bot.send_file(
                int(get_dump()),
                oo,
                force_document=True,
                thumb="thumb.jpg",
                caption=f"`{cap}`",
            )
        else:
            await bot.send_file(
                int(get_dump()), oo, force_document=True, caption=f"`{cap}`"
            )
        await x.edit("`Successfully Posted`")
        return
    await e.edit("`reply to any media , document and others.`")
