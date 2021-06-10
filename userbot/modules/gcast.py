# ©Copyright King-Userbot (Apis) USERBOT TELEGRAM
# Ported by Apis
# Thanks for ultroid

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.ggcast (.*)")
async def gcast(event):
    kinguser = event.pattern_match.group(1)
    if not kinguser:
        return await event.edit("`King, Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[6:]
    kingget = await event.edit("`Sedang Mengirim Pesan Secara Global...⚡️`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kingget.edit(f"**Sukses Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")


@register(outgoing=True, pattern="^.gucast (.*)")
async def gucast(event):
    lynxuser = event.pattern_match.group(1)
    if not lynxuser:
        return await event.edit("`Mohon Berikan Sebuah Pesan`")
    tt = event.text
    msg = tt[7:]
    lynxget = await event.edit("`Sedang Mengirim Pivate Messages Secara Global... 📢`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await lynxget.edit(f"**Sukses Mengirim Pesan Ke** `{done}` **Orang, Gagal Mengirim Pesan Ke** `{er}` **Orang.**")


CMD_HELP.update(
    {
        "gcast": "**✘ Plugin : **`Global Broadcast`\
        \n\n  •  **Perintah :** `.ggcast` <Text>`\
        \n  •  **Function : **Global Group Broadcast. Mengirim  Global Broadcast pesan ke Seluruh Grup yang king masuki\
        \n\n  •  **Perintah :** `.gucast` <Text>`\
        \n  •  **Function : **Global Users Broadcast. Kirim Pesan itu Secara Global ke Semua Anggota Group Anda.\
     "
    }
)
