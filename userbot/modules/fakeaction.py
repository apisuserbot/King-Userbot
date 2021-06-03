# Port By @VckyouuBitch From Geez-Projects
# Copyright (C) 2021 Geez-Project
from userbot.events import register
from userbot import CMD_HELP, HEROKU_APP_NAME, ALIVE_NAME
from time import sleep
import asyncio

# Languange en to id from King-Userbot
# edit by Apis
# Thanks Vicky


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai Pengetikan Palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai rekaman audio palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai perekaman video palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Mulai Bermain Game Palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fkuota(?: |$)(.*)")
async def _(event):
    await event.edit("`Mengecek kuota...⚡️`")
    sleep(1)
    await event.edit(
        f"★ **INFO KUOTA KING** ★\n╔══════━━━━━━━══════╗ \n"
        f"➠ **Penggunaan Kuota :** `{app.name}` \n"
        f"   • **Hasil :** `00` **Jam** - `00` **Menit** \n"
        f"   • **Persen :** `00`% \n"
        f"◖═══════════════════◗ \n"
        f"➠ **Sisa Kuota Bulan Ini :** \n"
        f"   • **Sisa :**  `1000` **Jam** - `10` **Menit** \n"
        f"   • **Persen :** `00`% \n"
        f"╚══════━━━━━━━══════╝ \n"
        f"◈ **KING  :** {ALIVE_NAME} \n"
        f"◈ **REPO :** [King-Userbot](https://github.com/apisuserbot/King-Userbot)")

CMD_HELP.update(
    {
        "fakeaction": "**✘ Plugin :** `fakeaction`\
        \n\n  •  **Perintah :** `.ftyping` | `.faudio` | `.fvideo` | `.fgame` <jumlah text>\
        \n  •  **Function : **Fake Ini Yang Bisa Menipu Saat Anda Mengetik , Audio , Video , Memainkan Game Selama Mungkin\
        \n\n  •  **Perintah :** `.fkuota`\
        \n  •  **Function : **Fake dyno Yang Bisa Menipu Saat Anda Mengetik `.fkuota` Yang Keluar 1000 Jam Dyno , Selamat Mencoba\
    "
    }
)
