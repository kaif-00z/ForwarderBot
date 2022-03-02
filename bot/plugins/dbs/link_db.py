from bot import dB


def get_link():
    return dB.get("LINK") or " "


def is_link():
    _ = dB.get("LINK") or " "
    if _.strip():
        return True
    return False
