from telethon import TelegramClient
API_KEY = "Harap Anda Memasukan API_KEY Dengan Benar"
API_HASH = "Harap Anda Memasukan API_HASH Dengan Benar"
# get it from my.telegram.org
bot = TelegramClient('userbot', API_KEY, API_HASH)
bot.start()

# This script wont run your bot, it just generates a session.
