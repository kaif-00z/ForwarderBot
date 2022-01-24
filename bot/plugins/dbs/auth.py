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

if Var.OWNER_ID:
    auth = eval(dB.get("AUTH_USERS") or "[]")
    if Var.OWNER_ID not in auth:
        auth.append(Var.OWNER_ID)
        dB.set("AUTH_USERS", str(auth))


def get_auth():
    return eval(dB.get("AUTH_USERS") or "[]")


def is_auth(id):
    if id in eval(dB.get("AUTH_USERS") or "[]"):
        return True
    return False


def add_auth(id):
    auth = eval(dB.get("AUTH_USERS") or "[]")
    if id not in auth:
        auth.append(id)
        dB.set("AUTH_USERS", str(auth))


def rem_auth(id):
    auth = eval(dB.get("AUTH_USERS") or "[]")
    if id in auth:
        auth.remove(id)
        dB.set("AUTH_USERS", str(auth))
