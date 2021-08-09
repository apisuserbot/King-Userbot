from telethon.tl.types import MessageEntityMentionName

from userbot.core.logger import logging
from utils.tools import edit_delete

LOGS = logging.getLogger("userbot")


async def get_user_from_event(
    event, kingevent=None, secondgroup=None, nogroup=False, noedits=False
):  # sourcery no-metrics
    if kingevent is None:
        kingevent = event
    if nogroup is False:
        if secondgroup:
            args = event.pattern_match.group(2).split(" ", 1)
        else:
            args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-")
                                    and user[1:].isnumeric()):
                user = int(user)
            if event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(
                        probable_user_mention_entity,
                        MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await event.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await event.client.get_entity(user)
                return user_obj, extra
    except Exception:
        pass
    try:
        if nogroup is False:
            if secondgroup:
                extra = event.pattern_match.group(2)
            else:
                extra = event.pattern_match.group(1)
        if event.is_private:
            user_obj = await event.get_chat()
            return user_obj, extra
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.from_id is None:
                if not noedits:
                    await edit_delete(kingevent, "`Well that's an anonymous admin !`")
                return None, None
            user_obj = await event.client.get_entity(previous_message.sender_id)
            return user_obj, extra
        elif not args:
            if not noedits:
                await edit_delete(
                    kingevent, "`Pass the user's username, id or reply!`", 5
                )
            return None, None
    except Exception as e:
        LOGS.error(str(e))
    if not noedits:
        await edit_delete(kingevent, "__Couldn't fetch user to proceed further__")
    return None, None
