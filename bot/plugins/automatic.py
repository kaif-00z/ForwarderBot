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

if os.path.isfile("thumb.jpg"):
    os.remove("thumb.jpg")
    if is_thumb():
        os.system(f"wget {get_thumb()} -O thumb.jpg")
        LOGS.info("successfully set the Thumbnail")
    else:
        LOGS.info("thumbnail is not set")
else:
    if is_thumb():
        os.system(f"wget {get_thumb()} -O thumb.jpg")
        LOGS.info("successfully set the Thumbnail")
    else:
        LOGS.info("thumbnail is not set")
