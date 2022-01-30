# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.hentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    await event.edit("```Sedang Memproses```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=424466890)
            )
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap buka blokir @nHentaiBot dan coba lagi```")
            return
        if response.text.startswith(
                "**Maaf, saya tidak bisa mendapatkan manga dari**"):
            await event.edit("```Saya pikir ini bukan tautan yang tepat king!```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "hentai": "**✘ Plugin : **`hentai`\
        \n\n  •  **Perintah :** `.hentai`\
        \n  •  **Function : **Melihat nhentai di telegra.ph XD\
    "
    }
)
