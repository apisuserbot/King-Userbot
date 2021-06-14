from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.events import register
from userbot import CMD_HELP


# Ported Apis Ganteng ( King - Userbot )
@register(outgoing=True, pattern="^.xban(?: |$)(.*)")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("Anda Tidak Mempunyai Hak")
        return
    await event.edit("Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Tidak Ada yang Terjadi di sini king:)")

CMD_HELP.update(
    {
        "xban": "**✘ Plugin : **`xban`\
        \n\n  •  **Perintah : **`.xban`\
        \n  •  **Function : **ban semua member dalam satu perintah\
        \n\n  **Peringatan :** __**Hati hati dalam penggunaan perintah , karena dalam sekejap perintah ini aktif semua member anda akan terbannned!**__\
    "
    }
)
