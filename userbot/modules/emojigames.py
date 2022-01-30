# fix by @PacarFerdilla for OUB
# remove and fixed

from telethon.tl.types import InputMediaDice
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice(""))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🎯"))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice("🏀"))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass


CMD_HELP.update(
    {
        "emojigames": "**✘ Plugin :** `Emoji Games`\
        \n\n  •  **Perintah :** `.dice` 1-6 atau `.dart` 1-6 atau `.ball` 1-5\
        \n  •  **Function : **Emoji Games Hanya Untuk Bersenang Senang\
        \n **WARNING :** __Jangan Di Salah Gunakan, Karena Userbot Bisa Crash__\
    "
    }
)
