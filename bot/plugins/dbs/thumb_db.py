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


from bot import dB


def set_thumb(thumb):
    dB.set("THUMBNAIL", str(thumb))


def get_thumb():
    return dB.get("THUMBNAIL") or " "


def is_thumb():
    _ = dB.get("THUMBNAIL") or " "
    if _.strip():
        return True
    return False
