from userbot import *
import asyncio
from userbot.events import register


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


@register(outgoing=True, pattern=r"\.(?:team|teamon)\s?(.)?")
async def _(event):
    await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await event.edit("...⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡...")
    output = (
        f"════════⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════\n"
        f"**Nama Creator Kami**\n"
        f"╟◈🛠️ Developer : [Apis](t.me/PacarFerdilla) \n"
        f"╟◈🛠️ Developer : [Abdul](t.me/lvufrvrbby) \n"
        f"╟◈👤 Contributor : [Rimuru](t.me/imbakaaaaa) \n"
        f"╰╼═══════════════════╾╯\n"
        f"**Terimakasih Telah Menggunakan Project Userbot Kami 🙏 \n"
        f"═════════⚡𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════════"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await event.delete()
            msg = await bot.send_file(event.chat_id, logo, caption=output)
            await asyncio.sleep(200)
            await msg.delete()
        except BaseException:
            await event.edit(
                output + "\n\n *`Link ke logo salah."
                "\nCoba untuk di cek ulang."
            )
            await asyncio.sleep(100)
            await event.delete()
    else:
        await event.edit(output)
        await asyncio.sleep(100)
        await event.delete()

CMD_HELP.update({
    "kingteam": "⚡𝘾𝙈𝘿⚡: `.team`"
    "\n↳ : Untuk mengetahui creator bot."
})