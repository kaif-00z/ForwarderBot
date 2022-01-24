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


from bot import Var, dB


def get_dump():
    return eval(dB.get("DUMP_CHANNEL") or " ")


"""
def add_dump(id):
    dump = eval(dB.get("DUMP_CHANNEL") or "[]")
    if id not in dump:
        dump.append(id)
        dB.set("DUMP_CHANNEL", str(id))


def rem_dump(id):
    dump = eval(dB.get("DUMP_CHANNEL") or "[]")
    if id not in dump:
        dump.remove(id)
        dB.set("DUMP_CHANNEL", str(id))
"""


def is_dump():
    _ = dB.get("DUMP_CHANNEL") or " "
    if _.strip():
        return True
    return False


if is_dump():
    pass
else:
    dB.set("DUMP_CHANNEL", str(Var.GROUP_ID))
