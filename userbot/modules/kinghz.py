# Based Code by @adekmaulana
# Improve by @aidilaryanto
# Apis Ganteng Banget
# Yang Ubah Kena Azab
import os
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY, CMD_HELP


@register(outgoing=True, pattern=r"^.hz(:? |$)(.*)?")
async def _(hazmat):
    await hazmat.edit("`King Ingin Mengaktifkan Perintah Hazmat...⚡`")
    level = hazmat.pattern_match.group(2)
    if hazmat.fwd_from:
        return
    if not hazmat.reply_to_msg_id:
        await hazmat.edit("`King, Mohon Balas Ke Sticker/Gambar`")
        return
    reply_message = await hazmat.get_reply_message()
    if not reply_message.media:
        await hazmat.edit("`Kata Bisa Menghancurkan Apapun LKing`")
        return
    chat = "@hazmat_suit_bot"
    await hazmat.edit("```Perintah Hazmat Diaktifkan, Sedang Memproses.... ⚡```")
    message_id_to_reply = hazmat.message.reply_to_msg_id
    msg_reply = None
    async with hazmat.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/hazmat {level}"
                msg_reply = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            elif reply_message.gif:
                m = "/hazmat"
                msg_reply = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await hazmat.reply("`King, Mohon Buka Blokir` @hazmat_suit_bot `Lalu Coba Lagi`")
            return
        if response.text.startswith("I can't"):
            await hazmat.edit("`Mohon Maaf King, GIF Tidak Bisa...`")
            await hazmat.client.delete_messages(
                conv.chat_id, [msg.id, response.id, r.id, msg_reply.id]
            )
            return
        else:
            downloaded_file_name = await hazmat.client.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await hazmat.client.send_file(
                hazmat.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            if msg_reply is not None:
                await hazmat.client.delete_messages(
                    conv.chat_id, [msg.id, msg_reply.id, r.id, response.id]
                )
            else:
                await hazmat.client.delete_messages(conv.chat_id, [msg.id, response.id])
    await hazmat.delete()
    return os.remove(downloaded_file_name)


CMD_HELP.update(
    {
        "hazmat": ">⚡𝘾𝙈𝘿⚡`.hz` atau >⚡𝘾𝙈𝘿⚡`.hz [flip, x2, rotate (level), background (nomer), black]`"
        "\nUsage: Balas ke gambar/sticker untuk menyesuaikan!"
    }
)
