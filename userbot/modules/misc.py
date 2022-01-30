# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
#
# Repository (King-Userbot)
""" Userbot module for other small commands. """

from random import randint
from time import sleep
from os import execl
import asyncio
import sys
import os
import io
import sys
from userbot import ALIVE_NAME, BOTLOG, BOTLOG_CHATID, BOT_VER, CMD_HELP, bot
from userbot.events import register
from userbot.utils import time_formatter
import urllib
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """For .random command, get a random item from the list of items."""
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 atau lebih item yang diperlukan! Periksa .help random untuk info lebih lanjut.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit(
        "**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`"
    )


@register(outgoing=True, pattern="^.sleep ([0-9]+)$")
async def sleepybot(time):
    """For .sleep command, let the userbot snooze for a few second."""
    counter = int(time.pattern_match.group(1))
    await time.edit("`Saya tidur dulu King...⚡️`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"Anda membuat bot tidur untuk bot {str_counter}.",
        )
    sleep(counter)
    await time.edit("`Oke , saya sudah bangun`")


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """For .shutdown command, shut the bot down."""
    await event.edit("`Mematikan King-Userbot....`")
    await asyncio.sleep(7)
    await event.delete()
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#SHUTDOWN \n" "`King-Userbot Telah Dimatikan`"
        )
    await bot.disconnect()


@register(outgoing=True, pattern="^.restart$")
async def killdabot(event):
    await event.edit("`Memulai ulang King-Userbot...`")
    await asyncio.sleep(10)
    await event.delete()
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#RESTARTBOT \n" "`King-Userbot Telah Di Mulai Ulang`"
        )
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@register(outgoing=True, pattern="^.readme$")
async def readme(e):
    await e.edit(
        "   **Readme Userbot** \n\n"
        "\n• **Repo** [King-Userbot](https://github.com/apisuserbot/King-Userbot/blob/King-Userbot/README.md)"
        "\n• **Repo** [WeebProject-Apis](https://github.com/apisuserbot/WeebProject-Apis/blob/WeebProject-Apis/README.md)"
    )


@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """For .repo command, just returns the repo URL."""
    await wannasee.edit(
        f"   **Repository Userbot** \n\n"
        "• **Repo Userbot :** [King-Userbot](https://github.com/apisuserbot/King-Userbot) \n"
        f"• **Versi Userbot :** `{BOT_VER}` \n"
        "• **License :** [Raphielscape Version 1.d](https://github.com/apisuserbot/King-Userbot/blob/King-Userbot/LICENSE) \n"
        "• **Developer Project :** [Apis](https://t.me/PacarFerdilla) \n\n"
        "**Support :** [USERBOT TELEGRAM](https://t.me/KingUserbotSupport) "
    )


@register(outgoing=True, pattern="^.string$")
async def string_is_here(wannasee):
    """For .string command, just returns the string URL."""
    await wannasee.edit(
        f"   **String Session Userbot** \n\n"
        "• **Get string session :** [String Session](https://replit.com/@apisuserbot/String-Session?v=1) \n\n"
        "**Support :** [USERBOT TELEGRAM](https://t.me/KingUserbotSupport) "
    )


@register(outgoing=True, pattern="^.tutorial$")
async def tutorial_is_here(wannasee):
    """For .tutorial command, just returns the tutorial URL."""
    await wannasee.edit(
        "    **Tutorial Userbot** \n\n"
        "• **Tutorial :** [Tutorial Deploy](https://t.me/TeamKingUserbot/16) \n\n"
        "**Support :** [USERBOT TELEGRAM](https://t.me/KingUserbotSupport) "
    )


@register(outgoing=True, pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit("`Periksa log userbot untuk data pesan yang didekodekan !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Inilah data pesan yang didekodekan !!`",
        )


@register(outgoing=True, pattern=r"^.reverse(?: |$)(\d*)")
async def okgoogle(img):
    """For .reverse command, Google search images and stickers."""
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await bot.download_media(message, photo)
    else:
        await img.edit("`Harap Balas Di Gambar King`")
        return

    if photo:
        await img.edit("`Sedang Memproses...`")
        try:
            image = Image.open(photo)
        except OSError:
            await img.edit("`Gambar tidak di dukung`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {
            "encoded_image": (
                name,
                open(
                    name,
                    "rb")),
            "image_content": ""}
        response = requests.post(
            searchUrl,
            files=multipart,
            allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await img.edit(
                "`Gambar berhasil diunggah ke Google. Mungkin.`"
                "\n`Sumber parsing sekarang. Mungkin.`"
            )
        else:
            await img.edit("`Google menyuruhku pergi.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await img.edit(f"[{guess}]({fetchUrl})\n\n`Sedang Mencari gambar...`")
        else:
            await img.edit("`Tidak dapat menemukan apa pun untuk pantat jelekmu.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(
                entity=await img.client.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=img,
            )
        except TypeError:
            pass
        await img.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})"
        )


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + \
                urllib.parse.quote_plus(similar_image.get("value"))
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


async def scam(results, lim):

    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break

    return imglinks


@register(outgoing=True, pattern=r"^\.send (.*)")
async def send(event):
    await event.edit("`Sedang Memproses...`")

    if not event.is_reply:
        return await event.edit("`Mohon Balas ke pesan King!`")

    chat = event.pattern_match.group(1)
    try:
        chat = await event.client.get_entity(chat)
    except (TypeError, ValueError):
        return await event.edit("`Link yang diberikan tidak valid!`")

    message = await event.get_reply_message()

    await event.client.send_message(entity=chat, message=message)
    await event.edit(f"`Mengirim pesan ini ke` `{chat.title}``!`")


CMD_HELP.update(
    {
        "send": "**✘ Plugin :** `send`\
        \n\n  •  **Perintah :** `.send`\
        \n  •  **Function : **Meneruskan pesan balasan ke obrolan tertentu tanpa tag Forwarded from. \
    "
    }
)

CMD_HELP.update(
    {
        "random": "**✘ Plugin :** `random`\
        \n\n  •  **Perintah :** `.random`\
        \n  •  **Function : **Dapatkan item acak dari daftar item. \
    "
    }
)

CMD_HELP.update(
    {
        "sleep": "**✘ Plugin :** `sleep`\
        \n\n  •  **Perintah :** `.sleep`\
        \n  •  **Function : **Biarkan ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️ tidur selama beberapa detik \
    "
    }
)


CMD_HELP.update(
    {
        "repo": "**✘ Plugin :** `Repository` ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
        \n\n  •  **Perintah :** `.repo`\
        \n  •  **Function : **Menampilan link Repository ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
        \n\n  •  **Perintah :** `.string`\
        \n  •  **Function : **Menampilan link String ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
        \n\n  • **Perintah :** `.tutorial`\
        \n  •  **Function : **Menampilkan link Tutorial ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
    "
    }
)


CMD_HELP.update(
    {
        "readme": "**✘ Plugin :** `Readme Pada Repository`\
        \n\n  •  **Perintah :** `.readme`\
        \n  •  **Function : **Menyediakan tautan untuk mengatur userbot dan pluginnya\
    "
    }
)


CMD_HELP.update(
    {
        "restart": "**✘ Plugin :** `Memulai Ulang` ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
        \n\n  •  **Perintah :** `.restart`\
        \n  •  **Function : **Untuk Memulai Ulang userbot.\
    "
    }
)


CMD_HELP.update(
    {
        "shutdown": "**✘ Plugin :** `shutdown`\
        \n\n  •  **Perintah :** `.shutdown`\
        \n  •  **Function : **Mematikan Userbot.\
    "
    }
)


CMD_HELP.update(
    {
        "raw": "**✘ Plugin :** `raw`\
        \n\n  •  **Perintah :** `.raw`\
        \n  •  **Function : **Dapatkan data berformat seperti JSON terperinci tentang pesan yang dibalas.\
    "
    }
)


CMD_HELP.update(
    {
        "repeat": "**✘ Plugin :** `repeat`\
        \n\n  •  **Perintah :** `.repeat`\
        \n  •  **Function : **Mengulangi teks untuk beberapa kali , Jangan bingung ini dengan spam.\
    "
    }
)
