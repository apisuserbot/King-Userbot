# recoding...

from userbot.modules.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from telethon.utils import get_display_name

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.addchat(?: $)(.*)")
async def echo(event):
    r = await event.get_reply_message()
    if r:
        user = r.sender_id
    else:
        try:
            user = event.text.split()[1]
            if user.startswith("@"):
                ok = await event.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await eod(event, "Reply To A user.")
    if is_echo(event.chat_id, user):
        return await eod(event, "Echo already activated for this user")
    addecho(event.chat_id, user)
    ok = await event.client.get_entity(user)
    user = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
    await eor(event, f"Activated Echo For {user}.")


@register(outgoing=True, pattern="^.rmchat(?: $)(.*)")
async def rm(event):
    r = await event.get_reply_message()
    if r:
        user = r.sender_id
    else:
        try:
            user = event.text.split()[1]
            if user.startswith("@"):
                ok = await event.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await eod(event, "Reply To A User.")
    if is_echo(event.chat_id, user):
        remove_echo(event.chat_id, user)
        ok = await event.client.get_entity(user)
        user = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
        return await eor(event, f"Deactivated Echo For {user}.")
    await eor(event, "Echo not activated for this user")


@bot.on(events.NewMessage(incoming=True))
async def okk(event):
    if is_echo(event.chat_id, event.sender_id):
        try:
            ok = await event.client.get_messages(event.chat_id, ids=e.id)
            return await event.client.send_message(event.chat_id, ok)
        except Exception as er:
            LOGS.info(er)


@register(outgoing=True, pattern="^.listchat(?: $)(.*)")
async def lstecho(event):
    k = get_all_echos(event.chat_id)
    if k:
        user = "**Activated Echo For Users :**\n\n"
        for x in k:
            ok = await event.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += "•" + kk + "\n"
        await eor(event, user)
    else:
        await eod(event, "`List is Empty, For echo`")


CMD_HELP.update(
    {
        "chat_follow": "**✘ Plugin :** `Chat Follow`\
        \n\n  •  **Perintah :** `.addchat`\
        \n  •  **Function : **Hampir Sama Dengan Echo , Cuman Ini Tidak Reply Pengguna\
    "
    }
)
