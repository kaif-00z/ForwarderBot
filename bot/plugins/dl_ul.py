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


@user.on(events.NewMessage(outgoing=True, pattern="\\.dl"))
async def _(event):
    if event.reply_to:
        fname = ""
        try:
            fname = f"downloads/{e.text.split()[1]}"
        except BaseException:
            pass
        x = await event.edit("`Downloading...`")
        ttt = time.time()
        reply = await event.get_reply_message()  # ignore pylint
        filename = f"downloads/{reply.file.name}"  # ignore pylint
        file = reply.document
        if fname:
            filename = fname
        with open(filename, "wb") as f:
            ok = await download_file(
                client=user,
                location=file,
                out=f,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "Downloading..")
                ),
            )
        await x.edit(f"`Successfully Downloaded`\n**Path** : `{filename}`")
        return
    await event.edit("`reply to any media , document and others.`")


@user.on(events.NewMessage(outgoing=True, pattern="\\.ul"))
async def _(event):
    path = ""
    ttt = time.time()
    x = event.edit("`Uploading...`")
    try:
        path = event.text.split()[1]
    except BaseException:
        pass
    if not path:
        return event.edit("Please give file path to upload")
    with open(path, "rb") as s:
        ok = await upload_file(
            client=user,
            file=s,
            name=path,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, x, ttt, "uploading..")
            ),
        )
    if os.path.isfile("thumb.jpg"):
        await user.send_file(
            event.chat_id,
            ok,
            force_document=True,
            thumb="thumb.jpg",
            caption=f"`{path}`",
        )
    else:
        await user.send_file(
            event.chat_id, ok, force_document=True, caption=f"`{path}`"
        )
    await x.edit("Successfully Uploaded the File")


@user.on(events.NewMessage(outgoing=True, pattern="\\.linkdl"))
async def _(e):
    link = f"downloads/{e.text.split()[1]}"
    x = e.edit("`Downloading...`")
    # cap = await fast_download(x, link)
    success, error = await bash(f"wget {link}")
    if error:
        return LOGS.info(str(error))
    await x.edit(f"Successfully Downloaded\n**Path** : `{link}`")


@bot.on(events.NewMessage(incoming=True, pattern="\\/dl"))
async def _(event):
    if not (is_auth(event.sender_id)):
        return
    if event.reply_to:
        fname = ""
        try:
            fname = f"downloads/{e.text.split()[1]}"
        except BaseException:
            pass
        x = await event.reply("`Downloading...`")
        ttt = time.time()
        reply = await event.get_reply_message()  # ignore pylint
        filename = f"downloads/{reply.file.name}"  # ignore pylint
        file = reply.document
        if fname:
            filename = fname
        with open(filename, "wb") as f:
            ok = await download_file(
                client=bot,
                location=file,
                out=f,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, x, ttt, "Downloading..")
                ),
            )
        await x.edit(f"`Successfully Downloaded`\n**Path** : `{filename}`")
        return
    await event.reply("`reply to any media , document and others.`")


@bot.on(events.NewMessage(incoming=True, pattern="\\/ul"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    path = ""
    ttt = time.time()
    x = event.reply("`Uploading...`")
    try:
        path = event.text.split()[1]
    except BaseException:
        pass
    if not path:
        return event.edit("Please give file path to upload")
    with open(path, "rb") as s:
        ok = await upload_file(
            client=bot,
            file=s,
            name=path,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, x, ttt, "uploading..")
            ),
        )
    if os.path.isfile("thumb.jpg"):
        await bot.send_file(
            event.chat_id,
            ok,
            force_document=True,
            thumb="thumb.jpg",
            caption=f"`{path}`",
        )
    else:
        await bot.send_file(event.chat_id, ok, force_document=True, caption=f"`{path}`")
    await x.delete()


@bot.on(events.NewMessage(incoming=True, pattern="\\/linkdl"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    link = f"downloads/{e.text.split()[1]}"
    x = e.reply("`Downloading...`")
    # cap = await fast_download(x, link)
    success, error = await bash(f"wget {link}")
    if error:
        return LOGS.info(str(error))
    await x.edit(f"Successfully Downloaded\n**Path** : `{link}`")
