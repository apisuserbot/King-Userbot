from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)
from telethon.tl.functions.channels import GetFullChannelRequest

from userbot.events import register
from userbot import CMD_HELP


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`channel/group tidak valid`")
            return None
        except ChannelPrivateError:
            await event.reply("`Ini adalah channel/group pribadi atau saya dibanned dari sana`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel atau supergroup tidak ada`")
            return None
        except (TypeError, ValueError):
            await event.reply("`channel/group tidak valid`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.inviteall(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        king = await event.reply("`Sedang Memproses...`")
    else:
        king = await event.edit("`Memproses...`")
    kingubot = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await king.edit("`Maaf, Tidak dapat menambahkan pengguna di sini`")
    s = 0
    f = 0
    error = 'None'

    await king.edit("**TerminalStatus**\n\n`Mengumpulkan Pengguna...`")
    async for user in event.client.iter_participants(kingubot.full_chat.id):
        try:
            if error.startswith("Too"):
                return await king.edit(f"**Terminal Kesalahan...**\n(`Mungkin Mendapat Kesalahan Batas dari telethon Tolong Coba Lagi`)\n**Error** : \n`{error}`\n\n• Menambahkan Pengguna `{s}`\n• Gagal Menambahkan Pengguna `{f}`")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await king.edit(f"**Terminal Berjalan...**\n\n• Menambahkan Pengguna `{s}`\n• Gagal Menambahkan Pengguna `{f}`\n\n**Kesalahan Terakhir :** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await king.edit(f"**Terminal Selesai** \n\n• Sukses Menambahkan Pengguna `{s}`\n• Gagal Menambahkan Pengguna `{f}`")


CMD_HELP.update(
    {
        "inviteall": "**✘ Plugin :** `Invite All`\
        \n\n  •  **Perintah :** `.inviteall` username group `@`\
        \n  •  **Function : **Menambahkan pengguna dari obrolan yang diberikan ke grup Anda\
    "
    }
)
