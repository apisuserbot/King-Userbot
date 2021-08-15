# Based Plugins
# Ported For King-Userbot By PacarFerdilla/Apis
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini Anjenggg!!!
# Done!
#
# Fixed

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()

# Apis Gans


@register(outgoing=True, pattern=r"^\.wp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Apis Gans


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Apis Gans


@register(outgoing=True, pattern=r"^\.truth(?: |$)(.*)")
async def _(event):
    await event.edit("`Bot Sedang Mengirimi Pesan!`")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/truth")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Harap unblock @truthordares_bot dan coba lagi`")
            return
        await event.edit(f"**Pesan Truth**\n\n{response.message.message}")

# Created Code By Apis


@register(outgoing=True, pattern=r"^\.dare(?: |$)(.*)")
async def _(event):
    await event.edit("`Bot Sedang Mengirimi Pesan!`")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/dare")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Harap unblock @truthordares_bot dan coba lagi`")
            return
        await event.edit(f"**Pesan Dare**\n\n{response.message.message}")

# Ported For King-Userbot By Apis

CMD_HELP.update(
    {
        "game": "**✘ Plugin :** `Game`\
        \n\n  •  **Perintah :** `.xogame`\
        \n  •  **Function : **Mainkan game XO bersama temanmu\
        \n\n  •  **Perintah :** `.mod` <nama app>\
        \n  •  **Function : **Dapatkan applikasi mod\
        \n\n  •  **Perintah :** `.wp` <teks> <username/ID>\
        \n  •  **Function : **Berikan pesan rahasia\
        \n\n  •  **Perintah :** `.truth` dan `.dare`\
        \n  •  **Function : **Mainkan Truth Or Dare Di Userbot Ini!\
    "
    }
)
