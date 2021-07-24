# from Ultroid import by @PacarFerdilla
# en to id by @PacarFerdilla
# Thanks Ultroid

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`King Gagal Dikarenakan Bukan Admin :)`"


async def get_call(event):
    king = await event.client(getchat(event.chat_id))
    user = await event.client(getvc(king.full_chat.call))
    return user.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Memulai Obrolan Suara...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("`Menghentikan Obrolan Suara...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(e):
    await e.edit("`Menambahkan Member Ke Obrolan Suara...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`Menambahkan {z} pengguna`")


CMD_HELP.update(
    {
        "calls": "**✘ Plugin :** `Calls Group`\
        \n\n  •  **Perintah :** `.startvc`\
        \n  •  **Function : **Memulai Obrolan Suara Dalam Grup\
        \n\n  •  **Perintah :** `.stopvc`\
        \n  •  **Function : **Memberhentikan Obrolan Suara Dalam Grup\
        \n\n  •  **Perintah :** `.vcinvite`\
        \n  •  **Function : **Menambahkan Semua Member Dalam Obrolan Suara Grup (Anda harus bergabung)\
    "
    }
)
