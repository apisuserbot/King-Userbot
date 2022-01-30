""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     **__⚡️BANTUAN⚡️__**     \n╚════════════╝ \n"
        f"**Hai King {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ developer  : [King Apis](t.me/PacarFerdilla) \n"
        "═⎆ Repository : [King-Userbot](https://github.com/apisuserbot/King-Userbot) \n"
        "═⎆ Instragam  : [Instagram King Apis](Instagram.com/apis_goodboy) \n"
        "═⎆ Grup Support : [King Userbot Support](https://t.me/KingUserbotSupport)"
    )


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  **__⚡️DAFTAR VARS⚡️__**     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari King** {DEFAULTUSER} :\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/varshelper.txt)"
    )


CMD_HELP.update(
    {
        "helper": "**✘ Plugin :** `Helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars\
    "
    }
)
