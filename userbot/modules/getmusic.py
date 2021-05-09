# Copyright (C) 2020 Aidil Aryanto.
# Vsong ported by AnggaR69S
# All rights reserved.
# Ported help plugin by Apis

import asyncio
import glob
import os
import time
from asyncio.exceptions import TimeoutError

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pylast import User
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeVideo

from userbot import CMD_HELP, LASTFM_USERNAME, bot, lastfm
from userbot.events import register
from userbot.utils import chrome, progress


async def getmusicvideo(cat):
    video_link = ""
    search = cat
    driver = await chrome()
    driver.get("https://www.youtube.com/results?search_query=" + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute("href")
        break
    command = 'youtube-dl -f "[filesize<50M]" --merge-output-format mp4 ' + video_link
    os.system(command)


@register(outgoing=True, pattern=r"^\.songn (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Error: Tidak ada scrobble saat ini yang ditemukan.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@WooMaiBot"
    link = f"/netease {track}"
    await event.edit("`Sedang Mencari...`")
    try:
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Sedang Mendownload...Mohon Tunggu`")
            try:
                msg = await conv.send_message(link)
                response = await conv.get_response()
                respond = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("```Tolong Buka Block @WooMaiBot Dan Coba Ulang```")
                return
            await event.edit("`Mengirim Musik Anda...`")
            await asyncio.sleep(3)
            await bot.send_file(event.chat_id, respond)
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, respond.id]
        )
        await event.delete()
    except TimeoutError:
        return await event.edit("`Error: `@WooMaiBot` tidak menanggapi!.`")


@register(outgoing=True, pattern=r"^\.songl(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Masukkan link yang valid untuk mendownload!`")
    else:
        await event.edit("`Mendownload...`")
    chat = "@MusicsHunterBot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(d_link)
                details = await conv.get_response()
                song = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Buka Block `@MusicsHunterBot` Dan Coba Ulang`")
                return
            await bot.send_file(event.chat_id, song, caption=details.text)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, details.id, song.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Error: `@MusicsHunterBot` tidak menanggapi!.`")


@register(outgoing=True, pattern=r"^\.songf (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Error: Tidak ada data scrobbling yang ditemukan.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Mendapatkan Musik Anda```")
    try:
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Mendownload...`")
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                msg = await bot.send_message(chat, track)
                respond = await response
                res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                r = await res
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Buka Block `@SpotifyMusicDownloaderBot` Dan Coba Ulang`")
                return
            await bot.forward_messages(event.chat_id, respond.message)
        await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
        await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@SpotifyMusicDownloaderBot` tidak menanggapi!.`"
        )


@register(outgoing=True, pattern=r"^\.vsong(?: |$)(.*)")
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("`Tunggu..! Saya menemukan lagu video Anda..`")
    elif reply:
        query = str(reply.message)
        await event.edit("`Tunggu..! Saya menemukan lagu video Anda..`")
    else:
        await event.edit("`Apa yang seharusnya saya temukan?`")
        return
    await getmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm"))
    if l:
        await event.edit("`Ya..! aku menemukan lagu..`")
    else:
        await event.edit(f"`Maaf..! saya tidak dapat menemukan apa pun dengan` **{query}**")
        return
    try:
        loa = l[0]
        metadata = extractMetadata(createParser(loa))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        os.system("cp *mp4 thumb.mp4")
        os.system("ffmpeg -i thumb.mp4 -vframes 1 -an -s 480x360 -ss 5 thumb.jpg")
        thumb_image = "thumb.jpg"
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            loa,
            force_document=False,
            thumb=thumb_image,
            allow_cache=False,
            caption=query,
            supports_streaming=True,
            reply_to=reply_to_id,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=width,
                    h=height,
                    round_message=False,
                    supports_streaming=True,
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "[UPLOAD]", loa)
            ),
        )
        await event.edit(f"**{query}** `Sukses Mengupload..!`")
        os.remove(thumb_image)
        os.system("rm *.mkv *.mp4 *.webm")
    except BaseException:
        os.remove(thumb_image)
        os.system("rm *.mkv *.mp4 *.webm")
        return


CMD_HELP.update(
    {
        "getmusic": "**✘ Plugin : **`getmusic`\
        \n\n  • **Perintah :** `.songn` <Artis - Nama Lagu>\
        \n  • **Function : **Untuk Mencari dan mendownload lagu dari youtube menggunakan bot @WooMaiBot.\
        \n\n  • **Perintah :** `.songl` <Spotify - Deezer Link>\
        \n  • **Function : **Untuk Mencari dan mendownload lagu  dari youtube menggunakan bot @MusicsHunterBot.\
        \n\n  • **Perintah : ** `.songf` <Artis - Nama Lagu>\
        \n  • ** Function: **Untuk Mencari dan mendownload lagu dari youtube menggunakan bot @SpotifyMusicDownloaderBot.\
        \n\n  • ** Perintah: ** `.songn now`\
        \n  • ** Function: **Mendownload Lagu LastFM menggunakan bot @WooMaiBot.\
        \n\n  • ** Perintah: ** `.songf now`\
        \n  • ** Function: **Mendownload Lagu LastFM menggunakan bot @SpotifyMusicDownloaderBot.\
        \n\n  • ** Perintah: ** `.vsong` <Artis - Nama Lagu>\
        \n  • ** Function: **Mengupload Sebuah Video Lagu Dari youtube.\
        "
    }
)
