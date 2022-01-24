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
from .dbs.thumb_db import *


@bot.on(events.NewMessage(incoming=True, pattern="\\/setthumb"))
async def _(e):
    if not (is_auth(e.sender_id)):
        return
    link = e.text.split()[1]
    if not is_thumb():
        set_thumb(link)
        if os.path.isfile("thumb.jpg"):
            os.remove("thumb.jpg")
            os.system(f"wget {get_thumb()} -O thumb.jpg")
            await e.reply("Successfully updated the Thumbnail")
        else:
            os.system(f"wget {get_thumb()} -O thumb.jpg")
            await e.reply("Successfully updated the Thumbnail")
    elif is_thumb():
        set_thumb(link)
        if os.path.isfile("thumb.jpg"):
            os.remove("thumb.jpg")
            os.system(f"wget {get_thumb()} -O thumb.jpg")
            await e.reply("Successfully updated the Thumbnail")
        else:
            os.system(f"wget {get_thumb()} -O thumb.jpg")
            await e.reply("Successfully updated the Thumbnail")
