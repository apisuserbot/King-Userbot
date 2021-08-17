# Yang Hapus Besok Mati Aminnn
# Port By @PacarFerdilla
# Apis Ganteng , Yang Hapus Meninggal Besok Aminn...
# Gabut Doang Gw Tod


from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.frog (.*)")
async def honkasays(event):
    await event.edit("`Sedang Memprosess!!!`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("`Beri Aku Bebeberapa Teks, Contoh .frog test`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`King! Saya tidak bisa menggunakan hal-hal sebaris di sini...`")
    except ChatSendStickersForbiddenError:
        await event.edit("Maaf King, saya tidak bisa mengirim stiker ke sini !!")


CMD_HELP.update(
    {
        "frog": "**✘ Plugin :** `Frog`\
        \n\n  •  **Perintah :** `.frog`\
        \n  •  **Function :** `.frog` <kata kata>\
    "
    }
)
