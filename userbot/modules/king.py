# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, ALIVE_LOGO, CMD_HELP
from userbot.events import register
from telethon import Button


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern="^.king(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit(
        f"`Halo {ALIVE_NAME} Saya Adalah Bot King Yang Menjaga Akun ini`"
        f"`Agar Terhindar Dari Orang Orang Jahat Di Telegram`"
        f"\n---------------------------------------------------"
        f"\n__**(C) copyright 2021 King-Userbot USERBOT TELEGRAM**__"
        f"\n\n**My King :** `{ALIVE_NAME}`")

# ------------->
logo = ALIVE_LOGO
# ------------->


@register(outgoing=True, pattern="^.repome$")
async def repo_inline_here(event):
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id == uid and query.startswith("@RepoMe"):
        result = builder.photo(
            file=logo,
            text=f"**King-Userbot**\n\n• **Support Chat :** [KLIK DISINI](https://t.me/KingUserbotSupport)\n• **Support Channel :** [KLIK DISINI](https://t.me/TeamKingUserbot)\n\n**USERBOT TELEGRAM**\n",
            buttons=[
                [
                    Button.url(
                        "Repository",
                        "https://github.com/apisuserbot/King-Userbot"),
                    Button.url(
                        "License",
                        "https://github.com/apisuserbot/King-Userbot/blob/King-Userbot/LICENSE")],
            ])

CMD_HELP.update(
    {
        "king": "**✘ Plugin :** `King`\
        \n\n  •  **Perintah :** `.king`\
        \n  •  **Function : **Perkenalan Userbot King\
        \n\n  •  **Perintah :** `.sadboy`\
        \n  •  **Function : **Jadi sadboy:)\
        \n\n  •  **Perintah :** `.punten` | `.pantau`\
        \n  •  **Function : **Untuk punten dan pantau\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @PacarFerdilla Jika ingin mengidekan sesuatu yang menarik **\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @PacarFerdilla Jika ingin mengidekan sesuatu yang menarik **\
    "
    }
)
