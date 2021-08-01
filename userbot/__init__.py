# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# inline credit @keselekpermen69
#
# Ported by Apis @PacarFerdilla
# Repository (King - Userbot)
""" Userbot initialization. """


import os
import time
import re
import platform
import psutil

from platform import python_version, uname
from datetime import datetime
from git import Repo
from time import sleep
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pymongo import MongoClient
from redis import StrictRedis
from dotenv import load_dotenv
from requests import get
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession
from telethon import Button, functions, types
from telethon.utils import get_display_name

load_dotenv("config.env")


StartTime = time.time()

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 9:
    LOGS.info("Anda HARUS memiliki versi python minimal 3.9"
              "Beberapa fitur bergantung pada ini, Bot berhenti.")
    quit(1)

# Periksa apakah konfigurasi telah diedit dengan menggunakan variabel yang sudah digunakan.
# Pada dasarnya, ini adalah 'pemeriksaan keperawanan' untuk file konfigurasi :)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Harap hapus baris yang disebutkan dalam tagar pertama dari file config.env"
    )
    quit(1)

# DEV and SUDO_USERS
DEVS = 1682708454, 1448477501, 1510613960, 1712864821, 1856628847,
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY", "")
API_HASH = os.environ.get("API_HASH", "")

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Custom Pmpermit text
PMPERMIT_TEXT = os.environ.get("PMPERMIT_TEXT", None)

# Custom Pmpermit pic
PMPERMIT_PIC = os.environ.get(
    "PMPERMIT_PIC",
    None) or "https://telegra.ph/file/ca73aa215579a60c700f3.jpg"

# Bleep Blop, this is a bot :)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", "")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/apisuserbot/King-Userbot.git")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "King-Userbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# untuk perintah .kingon
KING_TEKS_KUSTOM = os.environ.get("KING_TEKS_KUSTOM", None)

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Custom Emoji Alive
ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "⚡️")

# Custom Umur
UMUR = os.environ.get("UMUR", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "King-Userbot")

# Bot version
BOT_VER = os.environ.get("BOT_VER", "0.5.4")

# Default .alive username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/8eb368517a8d3933c05d9.jpg"

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius lyrics  API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None

# Init Mongo
MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)
MONGO = MONGOCLIENT.userbot


def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException:
        return False
    return True


# Init Redis
# Redis will be hosted inside the docker container that hosts the bot
# We need redis for just caching, so we just leave it to non-persistent
REDIS = StrictRedis(host='localhost', port=6379, db=0)


def is_redis_alive():
    try:
        REDIS.ping()
        return True
    except BaseException:
        return False


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER or not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "Anda harus menyiapkan BOTLOG_CHATID variabel di config.env atau environment variabel, agar penyimpanan log kesalahan pribadi berfungsi."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Akun Anda tidak memiliki hak untuk mengirim pesan ke BOTLOG_CHATID "
            "kelompok. Periksa apakah Anda mengetik ID Obrolan benar.")
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variabel bukan "
            "Identitas yang valid. Periksa Anda environment variabel/config.env atau file.")
        quit(1)


async def check_alive():
    await bot.send_message(BOTLOG_CHATID, "```⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡ Telah Aktif```")
    return

with bot:
    try:
        bot.loop.run_until_complete(check_alive())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variabel bukan "
            "Identitas yang valid. Periksa Anda environment variabel/config.env atau file.")
        quit(1)

# ==================================GlobalVariables================================= #

COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
king = bot
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}

# Import Userbot - Ported by Apis

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node

# --------------------------------------------InlineBot---------------------------------->


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 4
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline("{} {} |".format("|", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols],
                     modules[2::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⌫", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "☒", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "⌦", data="{}_next({})".format(prefix, modulo_page)
                )
            )
        ]
    return pairs


# -----------------------------------------------File------------------------------------>
king = bot

with king:
    try:
        king.tgbot = tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

# -----------------------------------------------File------------------------------------>
        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id
        logo = ALIVE_LOGO

        logoking = "https://telegra.ph/file/8b22cf95865c7ee798f7e.jpg"
        plugins = CMD_HELP

# ------------------------------ChatAction--------------->

        @king.tgbot.on(events.ChatAction)
        async def handler(event):
            if event.user_joined or event.user_added:
                u = await event.client.get_entity(event.chat_id)
                c = await event.client.get_entity(event.user_id)
                await event.reply(f"**Selamat datang di** [{get_display_name(u)}](tg://user?id={u.id})\n👤 **Pengguna :** [{get_display_name(c)}](tg://user?id={c.id})\n📌 **ID Pengguna :** {c.id}\n\nSemoga betah 😉")

# ====================================InlineHandler===================================== #

        @king.tgbot.on(events.NewMessage(pattern=r"/start"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                text = (
                    f"👋🏻 Hai [{get_display_name(u)}](tg://user?id={u.id}) Saya adalah bot\n"
                    f"Yang dibikin oleh pembuat saya,\n"
                    f"dan Untuk Mempersantai Grup Anda\n"
                    f"Saya **Dibuat oleh :** {DEFAULTUSER} pada heroku\n")
                await king.tgbot.send_file(event.chat_id, logo,
                                           caption=text,
                                           buttons=[
                                               [
                                                   custom.Button.url(
                                                       text="Support Chat",
                                                       url="https://t.me/KingUserbotSupport"),
                                                   custom.Button.url(
                                                       text="Support Channel",
                                                       url="https://t.me/TeamKingUserbot"
                                                   )
                                               ]
                                           ]
                                           )

        @king.tgbot.on(events.NewMessage(pattern=r"/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"👋🏻 Hai [{get_display_name(u)}](tg://user?id={u.id}) Jika anda\n"
                    f"Ingin melihat repository ini dan Cara deploynya\n\n"
                    f"👇🏻 `Klik button url di bawah ini` 👇🏻\n\n"
                    f"**USERBOT TELEGRAM**\n",
                    buttons=[
                        [
                            Button.url("Repository",
                                       "https://github.com/apisuserbot/King-Userbot"),
                            Button.url("Cara Deploy",
                                       "https://t.me/TeamKingUserbot/16")],
                    ]
                )

        @king.tgbot.on(events.NewMessage(pattern=r"/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await king.tgbot.send_message(
                    event.chat_id,
                    f"**PONG !!**\n `{ms}ms`",
                )

        @king.tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@KingUserbotSupport"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=logo,
                    link_preview=False,
                    text=f"\n⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡\n\n◎› **King** {DEFAULTUSER}\n\n◎› **Branch :** __King-Userbot__\n◎› **Versi Bot :** `v{BOT_VER}`\n◎› **Plugins :** `{len(plugins)}`\n\n**USERBOT TELEGRAM**".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan ⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡ ",
                    text="◎› Daftar Plugins",
                    buttons=[],
                    link_preview=True)
            else:
                result = builder.article(
                    "⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡",
                    text="""⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡\n\n**Anda Bisa Membuat King Userbot Anda Sendiri Dengan Cara :** [Tekan Disini](t.me/KingUserbotSupport)""",
                    buttons=[
                        [
                            custom.Button.url(
                                "King-Userbot",
                                "https://github.com/apisuserbot/King-Userbot"),
                            custom.Button.url(
                                "Developer",
                                "t.me/PacarFerdilla")],
                        [custom.Button.url(
                            "Tutorial Deploy",
                            "https://t.me/TeamKingUserbot/16")],
                    ],
                    link_preview=False,
                )
            await event.answer([result] if result else None)

# =============================================Button========================================= #

        @king.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"alive\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = f"\n==================================\n`Pengguna  :` {DEFAULTUSER}\n`Branch    :` {UPSTREAM_REPO_BRANCH}\n`Versi Bot :` {BOT_VER}\n`Bahasa    :` Python\n================================== "
                await event.edit(
                    text,
                    file=logo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("Repo Userbot",
                                       "https://github.com/apisuserbot/King-Userbot"),
                            Button.url("License",
                                       "https://github.com/apisuserbot/King-Userbot/blob/King-Userbot/LICENSE")],
                        [custom.Button.inline(
                            "Buka Menu", data="opener")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @king.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"opener")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                current_page_number = int(looters)
                buttons = paginate_help(current_page_number, plugins, "helpme")
                text = f"\n⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡\n\n◎› **King** {DEFAULTUSER}\n\n◎› **Branch :** __King-Userbot__\n◎› **Versi Bot :** `v{BOT_VER}`\n◎› **Plugins :** `{len(plugins)}`\n\n**USERBOT TELEGRAM**"
                await event.edit(text,
                                 file=logo,
                                 buttons=buttons,
                                 link_preview=False,
                                 )
            else:
                reply_pop_up_alert = f"🔒 Code Tersembunyi 🔒\n\nUserbot Milik {ALIVE_NAME} Yang Hanya Bisa Melihat Code Tersembunyi"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @king.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🔒 Code Tersembunyi 🔒\n\nUserbot Milik {ALIVE_NAME} Yang Hanya Bisa Melihat Code Tersembunyi"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @king.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = f"\n**USERBOT TELEGRAM**"
                await event.edit(
                    text,
                    file=logo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("Support Channel",
                                       "t.me/TeamKingUserbot"),
                            Button.url("Support Chat",
                                       "t.me/KingUserbotSupport")],
                        [Button.url("Donasi Developer",
                                    "https://saweria.co/DonasiDeveloper")],
                        [custom.Button.inline("Buka Menu", data="opener")],
                        [custom.Button.inline(
                            "Tutup Menu", b"close")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @king.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🔒 Code Tersembunyi 🔒\n\nUserbot Milik {ALIVE_NAME} Yang Hanya Bisa Melihat Code Tersembunyi"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @king.tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            if event.query.user_id == uid:
                text = f"\n**Menu Ditutup!**"
                await event.edit(
                    text,
                    file=logo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("Buka Menu", data="opener")],
                        [custom.Button.inline("Menu Alive", data="alive")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @king.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(b"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace('`', '')[:150] + "..."
                        + "\n\nBaca Teks Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} Tidak ada dokumen yang ditulis dari plugin.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = f"🔒 Code Tersembunyi 🔒\n\nUserbot Milik {ALIVE_NAME} Yang Hanya Bisa Melihat Code Tersembunyi"

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkan Pergi Ke @BotFather, lalu settings bot > pilih mode inline > Turn On. ")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variabel bukan "
            "Identitas yang valid. Periksa Anda environment variabel/config.env atau file.")
        quit(1)
