# Ported From Cat Userbot For King Userbot By Apis/PacarFerdilla # Jangan Hapus # Jangan Ubah Bangsat!!!
# Based On Plugins
# Apis Ganteng


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.deteksi(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await event.edit("```King, Mohon Balas Ke Pesan Pengguna atau ketik .deteksi (ID/Username) Yang mau Anda deteksi```")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit.event("`King, Mohon Berikan ID/Username untuk menemukan Riwayat`"
                                 )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await event.edit("`𝙈𝙚𝙣𝙙𝙚𝙩𝙚𝙠𝙨𝙞 𝙂𝙧𝙤𝙪𝙥 𝙋𝙚𝙣𝙜𝙜𝙪𝙣𝙖 𝙞𝙣𝙞...🔍`")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "``King Mohon Unblock @tgscanrobot Dan Coba Lagi```"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


# Apis Ganteng
CMD_HELP.update({
    "deteksi":
        "⚡𝘾𝙈𝘿⚡`.deteksi`\
          \nPenjelasan: Melihat Riwayat Grup Yang Pernah/Sedang dimasuki."
})
