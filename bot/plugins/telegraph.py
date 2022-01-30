from telegraph import Telegraph
from telegraph import upload_file as uf

from . import *

telegraph = Telegraph()
telegraph.create_account(short_name="Bot")


@bot.on(events.NewMessage(incoming=True, pattern="/telegraph"))
async def _(event):
    if not (is_auth(event.sender_id)):
        return
    if not event.reply_to:
        return await event.reply("`Plz Reply to photo,gif,media`")
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        if msg.photo or msg.video or msg.gif:
            getit = await bot.download_media(msg)
            try:
                variable = uf(getit)
                os.remove(getit)
                nn = "https://telegra.ph" + variable[0]
                await event.reply(f"Uploaded to [Telegraph]({nn}) !")
            except Exception as e:
                LOGS.info(str(e))
                await event.reply(f"Error Occurred - {e}")


@user.on(events.NewMessage(outgoing=True, pattern=".telegraph"))
async def _(event):
    if not event.reply_to:
        return await event.edit("`Plz Reply to photo,gif,media`")
    if event.reply_to_msg_id:
        msg = await event.get_reply_message()
        if msg.photo or msg.video or msg.gif:
            getit = await user.download_media(msg)
            try:
                variable = uf(getit)
                os.remove(getit)
                nn = "https://telegra.ph" + variable[0]
                await event.edit(f"Uploaded to [Telegraph]({nn}) !")
            except Exception as e:
                LOGS.info(str(e))
                await event.edit(f"Error Occurred - {e}")
