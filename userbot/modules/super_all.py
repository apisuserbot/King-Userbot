from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.events import register
from userbot import CMD_HELP


# Ported Apis Ganteng ( King - Userbot )
@register(outgoing=True, pattern="^.xban(?: |$)(.*)")
async def allban(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("`Anda Tidak Mempunyai Hak`")
        return
    await event.edit("`Sedang Membanned Semua Member Dalam Grup Ini...`")
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
    await event.edit("**Sukses, Anda Telah Membanned Semua Member Disini**")


@register(outgoing=True, pattern="^.xkick(?: |$)(.*)")
async def allkick(event):
    kinguser = await event.get_chat()
    kingget = await event.client.get_me()
    admin = kinguser.admin_rights
    creator = kinguser.creator
    if not admin and not creator:
        await event.edit("`Anda Tidak Mempunyai Hak`")
        return
    await event.edit("`Sedang Mengeluarkan Semua Member Dalam Grup Ini...`")

    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == kingget.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("**Sukses, Anda Telah Menendang Semua Member Disini**")

CMD_HELP.update(
    {
        "xall": "**✘ Plugin :** `Super All`\
        \n\n  •  **Perintah :** `.xban`\
        \n  •  **Function : **banned semua member dalam satu perintah\
        \n\n  •  **Perintah :** `.xkick`\
        \n  •  **Function : **Mengeluarkan semua member dalam satu perintah\
        \n\n   **Peringatan :** __**Hati hati dalam penggunaan perintah ini, karena dalam sekejap perintah ini aktif semua member anda akan terbannned atau terkeluarkan**__\
    "
    }
)
