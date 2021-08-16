# Ported info by Apis
# Thanks Ultroid limited

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.info(?: |$)(.*)")
async def _(event):
    await event.edit("`Mengecek Info Akun Anda...`")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Harap unblock @SpamBot dan coba lagi`")
            return
        await event.edit(f"**Pesan Info Akunmu**\n\n{response.message.message}")


CMD_HELP.update(
    {
        "info": "**✘ Plugin :** `Info`\
        \n\n  •  **Perintah :** `.info`\
        \n  •  **Function : **Untuk mengecek info akun Anda\
    "
    }
)
