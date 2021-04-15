# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


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
    """ For .ping command, ping the userbot from any chat.  """
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
                    f"〠 __My__ **KING** __|━|⎆__ ヅ "
                    f"\n  ☞ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.kping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡")
    await pong.edit("__**...💠KING💠...**__")
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
    await pong.edit(f"**╰━❖  king ping ❖━╯**\n"
                    f"☞ __ping:__ "
                    f"`%sms` \n"
                    f"☞ __i'm online:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`.....⚡King⚡.....`")
    await pong.edit("`⚡️`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"•⎚• ⎆ __King__ **Pong!**\n"
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
    await pong.edit("**...................**")
    await pong.edit("**DUARRR!**")
    await pong.edit("**................**")
    await pong.edit("⚡️")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"卍════〠 **TEST PING** 〠════卍\n"
                    f"═⎆ **Ping:** "
                    f"`%sms` \n"
                    f"═⎆ **Sisa Waktu:** "
                    f"`{uptime}` \n"
                    f"**✠➲ King:** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
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
                    f"__|━|⎆__ **My king  :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.uping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`.....☞KING Userbot☜.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"┏━━| **KING PONG** |━━卍\n"
                    f"┣|•  __Ping:__ "
                    f"`%sms` \n"
                    f"┗|• __Uptime:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "🛠 **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "⚙️ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "⚙️ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "⚙️ **Ping:** "
                   f"`{result['ping']}` \n"
                   "⚙️ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "⚙️ **BOT:** `⚡King Userbot⚡`")


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
    await pong.edit("⎚⎆ __King__ **Test Ping!**\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "⚡𝘾𝙈𝘿⚡`.ping` ; ⚡𝘾𝙈𝘿⚡`.kping` ; ⚡𝘾𝙈𝘿⚡`.xping` ; ⚡𝘾𝙈𝘿⚡`.fping`\
    \nPenjelasan: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nPenjelasan: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nPenjelasan: sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "**Modules:** `Sinyal`\
    \n\n**⚡𝘾𝙈𝘿⚡: `.sinyal`\
    \n  •**Penjelasan :** __Untuk melihat sinyal bot__"})
