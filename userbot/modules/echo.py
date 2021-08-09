# Thanks Sandy
# Recode By Apis

from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events

from userbot.utils import edit_delete, edit_or_reply
from userbot.modules.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    get_echos,
    is_echo,
    remove_all_echos,
    remove_echo,
    remove_echos,
)
from userbot.utils.events import get_user_from_event


@register(outgoing=True, pattern=r"^\.addecho(?: |$)(.*)")
async def echo(event):
    if event.reply_to_msg_id is None:
        return await edit_or_reply(
            event, "`Reply to a User's message to echo his messages`"
        )
    kingevent = await edit_or_reply(event, "`Adding Echo to user...`")
    user, rank = await get_user_from_event(event, kingevent, nogroup=True)
    if not user:
        return
    reply_msg = await event.get_reply_message()
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = user.first_name
        chat_type = "Personal"
    else:
        chat_name = event.chat.title
        chat_type = "Group"
    user_name = user.first_name
    user_username = user.username
    if is_echo(chat_id, user_id):
        return await edit_or_reply(event, "The user is already enabled with echo ")
    try:
        addecho(
            chat_id,
            user_id,
            chat_name,
            user_name,
            user_username,
            chat_type)
    except Exception as e:
        await edit_delete(kingevent, f"**Error:**\n`{str(e)}`")
    else:
        await edit_or_reply(kingevent, "Hi")


@register(outgoing=True, pattern=r"^\.rmecho(?: |$)(.*)")
async def echo(event):
    if event.reply_to_msg_id is None:
        return await edit_or_reply(
            event, "Reply to a User's message to echo his messages"
        )
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if is_echo(chat_id, user_id):
        try:
            remove_echo(chat_id, user_id)
        except Exception as e:
            await edit_delete(kingevent, f"**Error:**\n`{str(e)}`")
        else:
            await edit_or_reply(event, "Echo has been stopped for the user")
    else:
        await edit_or_reply(event, "The user is not activated with echo")


@register(outgoing=True, pattern=r"^\.delecho(?: |$)(.*)")
async def echo(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = get_all_echos()
        if len(lecho) == 0:
            return await edit_delete(
                event, "You havent enabled echo atleast for one user in any chat."
            )
        try:
            remove_all_echos()
        except Exception as e:
            await edit_delete(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await edit_or_reply(
                event, "Deleted echo for all enabled users in all chats."
            )
    else:
        lecho = get_echos(event.chat_id)
        if len(lecho) == 0:
            return await edit_delete(
                event, "You havent enabled echo atleast for one user in this chat."
            )
        try:
            remove_echos(event.chat_id)
        except Exception as e:
            await edit_delete(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await edit_or_reply(
                event, "Deleted echo for all enabled users in this chat"
            )


@register(outgoing=True, pattern=r"^\.listecho(?: |$)(.*)")
async def echo(event):  # sourcery no-metrics
    input_str = event.pattern_match.group(1)
    private_chats = ""
    output_str = "**Echo enabled users:**\n\n"
    if input_str:
        lsts = get_all_echos()
        group_chats = ""
        if len(lsts) > 0:
            for echos in lsts:
                if echos.chat_type == "Personal":
                    if echos.user_username:
                        private_chats += f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                    else:
                        private_chats += (
                            f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                        )
                else:
                    if echos.user_username:
                        group_chats += f"☞ [{echos.user_name}](https://t.me/{echos.user_username}) in chat {echos.chat_name} of chat id `{echos.chat_id}`\n"
                    else:
                        group_chats += f"☞ [{echos.user_name}](tg://user?id={echos.user_id}) in chat {echos.chat_name} of chat id `{echos.chat_id}`\n"

        else:
            return await edit_or_reply(event, "There are no echo enabled users")
        if private_chats != "":
            output_str += "**Private Chats**\n" + private_chats + "\n\n"
        if group_chats != "":
            output_str += "**Group Chats**\n" + group_chats
    else:
        lsts = get_echos(event.chat_id)
        if len(lsts) <= 0:
            return await edit_or_reply(
                event, "There are no echo enabled users in this chat"
            )

        for echos in lsts:
            if echos.user_username:
                private_chats += (
                    f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                )
            else:
                private_chats += (
                    f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                )
        output_str = f"**Echo enabled users in this chat are:**\n" + private_chats

    await edit_or_reply(event, output_str)


@bot.on(events.NewMessage(incoming=True, edited=False))
async def samereply(event):
    if is_echo(event.chat_id, event.sender_id) and (
        event.message.text or event.message.sticker
    ):
        await event.reply(event.message)

CMD_HELP.update(
    {
        "echo": "**Plugin :** `Echos`\
        \n\n  •  **Perintah :** `.addecho`\
        \n  •  **Function : **Untuk Menambahkan Follower Chat Pengguna\
    "
    }
)
