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


def ban(id):
    ban = eval(dB.get("BAN_USERS") or "[]")
    if id not in ban:
        ban.append(id)
        dB.set("BAN_USERS", str(ban))


def unban(id):
    ban = eval(dB.get("BAN_USERS") or "[]")
    if id in ban:
        ban.remove(id)
        dB.set("BAN_USERS", str(ban))


def is_ban(id):
    ban = eval(dB.get("BAN_USERS") or "[]")
    if id in ban:
        return True
    return False


def get_ban_user():
    return eval(dB.get("BAN_USERS") or "[]")
