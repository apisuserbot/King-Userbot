# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import time

from datetime import datetime
from telethon import functions

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
from userbot.utils import humanbytes


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.fping$")
async def pingme(pong):
    """ For .fping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"〠 __Test__ **PING** __|━|⎆__ ヅ "
                    f"\n  ☞ `%sms` \n"
                    f"〠 __My__ **LORD** __|━|⎆__ ヅ "
                    f"\n  ☞ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.kping$")
async def pingme(pong):
    """ For .kping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡")
    await pong.edit("__**...💠AB KING💠...**__")
    await pong.edit("__**.....USERBOT.....**__")
    await pong.edit("__**......MOHON MENUNGGU......**__")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**╰━❖  Lord Ping ❖━╯**\n"
                    f"☞ __ping:__ "
                    f"`%sms` \n"
                    f"☞ __i'm online:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .xping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`.....⚡LORD⚡.....`")
    await pong.edit("`⚡️`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"•⎚• ⎆ __Lord__ **Pong!**\n"
                    f"☞  __Ping:__ "
                    f"`%sms` \n"
                    f"☞  __Sisa Waktu:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Memulai Test Sinyal**")
    await pong.edit("**..Mohon menunggu..**")
    await pong.edit("**...❤️‍🔥『AB』 Ӄᴇꮯᴇꪎꤪ Lord❤️‍🔥...**")
    await pong.edit("**...................**")
    await pong.edit("**DUARRR MEMEK!**")
    await pong.edit("**................**")
    await pong.edit("**¸„.-•~¹°”¹⁸⁺ˆ˜¨『A̶̢̹̩̯̗̰̣͔̠͛̐͒͛̐̒̐̌ ̸̝͎̦́̔͠Β̸͌͂̑̆𖣘』×፝֟͜×◦𖤍𝙰͠ɴᴛͫʜͣ𒆜𓆩ɴʀᵈ᭄𓆪ꗄ¨˜ˆ¹⁸⁺”°¹~•-.„¸**")
    await pomg.edit("**....Sabar Lord.......**")
    await pong.edit("⚡️")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"卍════〠 **TEST PING TOD** 〠════卍\n"
                    f"═⎆ **Ping:** "
                    f"`%sms` \n"
                    f"═⎆ **Sisa Waktu:** "
                    f"`{uptime}` \n"
                    f"**✠➲ Lord:** `{ALIVE_NAME}`" % (duration))
    f"═⎆ **Pesan:Pap Tengktopnya Kakak🥰🥰**"


@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .sinyal command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"- K I N G -\n"
                    f"**☞ sinyal  :** "
                    f"`%sms` \n"
                    f"**☞ i'm online  :** "
                    f"`{uptime}` \n"
                    f"__|━|⎆__ **My Lord  :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.uping$")
async def pingme(pong):
    """ For .uping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__KING__")
    await pong.edit("__PONG__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┏━━| **LORD PONG** |━━卍\n"
                    f"┣|•  __Ping:__ "
                    f"`%sms` \n"
                    f"┗|• __Uptime:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^!ping$")
async def pingme(pong):
    """ For !ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Pinging...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**𓆩Lord𓆪** ╚» {ALIVE_NAME}\n\n"
                    f"**Pong !!** "
                    f"`%sms` \n"
                    f"**Uptime** - "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.jaringan$")
async def speedtst(spd):
    """ For .jaringan command, use SpeedTest to check server speeds. """
    await spd.edit("`Mengecek Tes jaringan...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil jaringan:\n**"
                   "🛠 **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" ━━━━━━━━━━━━━━━━━\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Ping:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✧ **BOT:** ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\n\n"
                   f" ━━━━━━━━━━━━━━━━━ ")


# Port WeebProject
@register(outgoing=True, pattern=r"^\.speedtest$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    await spd.edit("`Menjalankan Speed Test...🚀`")

    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    msg = (
        f"**Dimulai pada {result['timestamp']}**\n\n"
        "**Klien**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Negara :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Nama :** `{result['server']['name']}`\n"
        f"**Negara :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )

    await spd.delete()
    await spd.client.send_file(
        spd.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@register(outgoing=True, pattern=r"^\.dc$")
async def neardc(event):
    """For .dc command, get the nearest datacenter information."""
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(
        f"Negara : `{result.country}`\n"
        f"Pusat Data Terdekat : `{result.nearest_dc}`\n"
        f"Pusat Data ini : `{result.this_dc}`"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong...........🏎`")
    await pong.edit("`Pong..........🏎.`")
    await pong.edit("`Pong.........🏎..`")
    await pong.edit("`Pong........🏎...`")
    await pong.edit("`Pong.......🏎....`")
    await pong.edit("`Pong......🏎.....`")
    await pong.edit("`Pong.....🏎......`")
    await pong.edit("`Pong....🏎.......`")
    await pong.edit("`Pong...🏎........`")
    await pong.edit("`Pong..🏎.........`")
    await pong.edit("`Pong.🏎..........`")
    await pong.edit("`Pong🏎...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("⎚⎆ __Lord__ **Test Ping!**\n`%sms`" % (duration))

CMD_HELP.update(
    {
        "ping": "**✘ Plugin : **`ping`\
        \n\n  •  **Perintah :** `.ping` | `kping` | `.xping` | `.sinyal` | `.uping`\
        \n  •  **Function :** Untuk menunjukkan ping userbot.\
        \n\n  •  **Perintah :** `.pong`\
        \n  •  **Function :** Sama seperti perintah ping\
        \n\n  •  **Perintah :** `.jaringan`\
        \n  •  **Function :** Untuk Mengetes jaringan userbot.\
        \n\n  •  **Perintah :** `.speedtest` | `.dc`\
        \n  •  **Function :** Untuk Mengetes Server Userbot\
        \n\n  •  **Perintah :** `!ping`\
        \n  •  **Function : **Pingnya hampir sama dengan ultroid namun ini versi king!\
    "
    }
)
