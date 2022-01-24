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
from bot.config import Var


def get_req():
    _ = dB.get("REQUEST") or " "
    if "True" == _:
        return True
    return False


def get_req_channel():
    return eval(dB.get("REQUEST_CHANNEL") or " ")


def is_req_channel():
    _ = dB.get("REQUEST_CHANNEL") or " "
    if _.strip():
        return True
    return False


if is_req_channel():
    pass
else:
    dB.set("REQUEST_CHANNEL", str(Var.LOG_CHANNEL))
