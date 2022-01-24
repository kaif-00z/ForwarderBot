import io
import pprint
import traceback

from . import *


@bot.on(events.NewMessage(incoming=True, pattern="\\bash"))
async def _(event):
    if event.sender_id != Var.OWNER_ID:
        if event.sender_id != Var.DEV:
            return
    xx = await event.reply("`Processing...`")
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await xx.delete()
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    stdout, stderr = await bash(cmd)
    OUT = f"**☞ BASH\n\n• COMMAND:**\n`{cmd}` \n\n"
    if stderr:
        OUT += f"**• ERROR:** \n`{stderr}`\n\n"
    if stdout:
        _o = stdout.split("\n")
        o = "\n".join(_o)
        OUT += f"**• OUTPUT:**\n`{o}`"
    if not stderr and not stdout:
        OUT += "**• OUTPUT:**\n`Success`"
    if len(OUT) > 4096:
        ultd = OUT.replace("`", "").replace("**", "").replace("__", "")
        with io.BytesIO(str.encode(ultd)) as out_file:
            out_file.name = "bash.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )

            await xx.delete()
    else:
        await xx.edit(OUT)


p, pp = print, pprint  # ignore: pylint


@bot.on(events.NewMessage(incoming=True, pattern="\\.eval"))
async def _(event):
    if event.sender_id != Var.OWNER_ID:
        if event.sender_id != Var.DEV:
            return
    xx = await event.reply("`Processing...`")
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await xx.delete()
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = event.message.id
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Succcess"
    final_output = (
        "__►__ **EVAL**\n```{}``` \n\n __►__ **OUTPUT**: \n```{}``` \n".format(
            cmd,
            evaluation,
        )
    )
    if len(final_output) > 4096:
        ultd = final_output.replace("`", "").replace("**", "").replace("__", "")
        with io.BytesIO(str.encode(ultd)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=f"```{cmd}```" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
            await xx.delete()
    else:
        await xx.edit(final_output)


async def aexec(code, event):
    exec(
        (
            (
                ("async def __aexec(e, client): " + "\n message = event = e")
                + "\n reply = await event.get_reply_message()"
            )
            + "\n chat = (await event.get_chat()).id"
        )
        + "".join(f"\n {l}" for l in code.split("\n"))
    )

    return await locals()["__aexec"](event, event.client)
