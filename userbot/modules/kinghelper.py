""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"**Hai King {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Mastah](t.me/PacarFerdilla)"
        "\n[Repo](https://github.com/apisuserbot/King-Userbot)"
        "\n[Instagram Mastah](Instagram.com/goodboy_)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/varshelper.txt)")


CMD_HELP.update({
    "kinghelper":
    "⚡𝘾𝙈𝘿⚡`.kinghelp`\
\nPenjelasan: Bantuan Untuk King-Userbot.\
\n⚡𝘾𝙈𝘿⚡`.kingvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
