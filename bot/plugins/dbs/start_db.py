from bot import dB

def set_start_message(msg):
    dB.set("START_MSG", msg)

def del_start_message():
    dB.delete("START_MSG")

def set_help_message(msg):
    dB.set("HELP_MSG", msg)

def del_help_message():
    dB.delete("HELP_MSG")
