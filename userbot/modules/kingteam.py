from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r'^\.team(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**..Terkoneksi Ke Creator..**")
    sleep(3)
    await typew.edit("..⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡..")
    sleep(2)
    await typew.edit(
        "════════⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════\n"
        "**Nama Creator Kami**\n"
        "╟◈🛠️ Developer : [Apis](t.me/PacarFerdilla) \n"
        "╟◈🛠️ Developer : [Abdul](t.me/lvufrvrbby) \n"
        "╟◈👤 Contributor : [Rimuru](t.me/imbakaaaaa) \n"
        "╰╼═══════════════════╾╯\n"
        "**Terimakasih Telah Menggunakan Project Userbot Kami 🙏 \n"
        "═════════⚡𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════════\n"



CMD_HELP.update({"kingteam": ">⚡️𝘾𝙈𝘿⚡️`.team`"
                 "\nUsage: Nama creator"
