from time import sleep
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.team$")
async def reedme(e):
    await event.edit(
        "════════⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════\n"
        "**Nama Creator Kami**\n"
        "╟◈🛠️ Developer : [Apis](t.me/PacarFerdilla) \n"
        "╟◈🛠️ Developer : [Abdul](t.me/lvufrvrbby) \n"
        "╟◈👤 Contributor : [Rimuru](t.me/imbakaaaaa) \n"
        "╰╼═══════════════════╾╯\n"
        "**Terimakasih Telah Menggunakan Project Userbot Kami 🙏 \n"
        "═════════⚡𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════════\n"



CMD_HELP.update({"kingteam": ">⚡️𝘾𝙈𝘿⚡️`.team`\
                 \nUsage: Nama creator"})
