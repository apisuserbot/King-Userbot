# Port By @VckyouuBitch From Geez-Projects
# Copyright (C) 2021 Geez-Project

from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP
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

# created by Apis


@register(outgoing=True, pattern="^.fkuota(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit("`Mengecek kuota...⚡️`")
    sleep(1)
    await event.edit(
        f"★ **INFO KUOTA KING** ★\n╔══════━━━━━━━══════╗ \n"
        f"➠ **Penggunaan Kuota :** `{ALIVE_NAME}` \n"
        f"• **Hasil :** `00` **Jam** - `00` **Menit** \n"
        f"• **Persen :** `00`% \n"
        f"◖═══════════════════◗ \n"
        f"➠ **Sisa Kuota Bulan Ini :** \n"
        f"• **Sisa :**  `1000` **Jam** - `00` **Menit** \n"
        f"• **Persen :** `10`% \n"
        f"╚══════━━━━━━━══════╝ \n"
        f"◈ **KING :** {ALIVE_NAME} \n"
        f"◈ **REPO :** [King-Userbot](https://github.com/apisuserbot/King-Userbot)")


@register(outgoing=True, pattern="^.fgban(?: |$)(.*)")
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("Set G_BAN_LOGGER_GROUP in vars otherwise module won't work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await bot.send_message(
            G_BAN_LOGGER_GROUP,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**gbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**User gbanned by {DEFAULTUSER}**")
    asyncio.sleep(5)
    await event.delete()


@register(outgoing=True, pattern="^.fungban(?: |$)(.*)")
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("Set G_BAN_LOGGER_GROUP in vars otherwise module won't work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await bot.send_message(
            G_BAN_LOGGER_GROUP,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**ungbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**User ungbanned by {DEFAULTUSER}**")
    asyncio.sleep(5)
    await event.delete()


CMD_HELP.update(
    {
        "fakeaction": "**✘ Plugin :** `fakeaction`\
        \n\n  •  **Perintah :** `.ftyping` | `.faudio` | `.fvideo` | `.fgame` <jumlah text>\
        \n  •  **Function : **Fake Ini Yang Bisa Menipu Saat Anda Mengetik , Audio , Video , Memainkan Game Selama Mungkin\
        \n\n  •  **Perintah :** `.fkuota`\
        \n  •  **Function : **Fake dyno 1000 jam\
        \n\n  •  **Perintah :** `.fgban`\
        \n  •  **Function : **Fake global banned\
        \n\n  •  **Perintah :** `.fungban`\
        \n  •  **Function : **Fake unglobal banned\
    "
    }
)
