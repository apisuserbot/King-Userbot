# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module for managing events. One of the main components of the userbot."""

import codecs
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

import requests
from telethon import events

from userbot import bot, BOTLOG_CHATID, LOGSPAMMER


def register(**args):
    """Register a new event."""
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", False)
    ignore_unsafe = args.get("ignore_unsafe", False)
    unsafe_pattern = r"^[^/!#@\$A-Za-z]"
    groups_only = args.get("groups_only", False)
    trigger_on_fwd = args.get("trigger_on_fwd", False)
    disable_errors = args.get("disable_errors", False)
    insecure = args.get("insecure", False)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    if "ignore_unsafe" in args:
        del args["ignore_unsafe"]

    if "groups_only" in args:
        del args["groups_only"]

    if "disable_errors" in args:
        del args["disable_errors"]

    if "trigger_on_fwd" in args:
        del args["trigger_on_fwd"]

    if "insecure" in args:
        del args["insecure"]

    if pattern:
        if not ignore_unsafe:
            args["pattern"] = pattern.replace("^.", unsafe_pattern, 1)

    def decorator(func):
        async def wrapper(check):
            if check.edit_date and check.is_channel and not check.is_group:
                # Messages sent in channels can be edited by other users.
                # Ignore edits that take place in channels.
                return
            if not LOGSPAMMER:
                send_to = check.chat_id
            else:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return

            try:
                from userbot.modules.sql_helper.blacklist_sql import get_blacklist

                for blacklisted in get_blacklist():
                    if str(check.chat_id) == blacklisted.chat_id:
                        return
            except Exception:
                pass

            if check.via_bot_id and not insecure and check.out:
                return

            try:
                await func(check)

            # Thanks to @kandnub for this HACK.
            # Raise StopPropagation to Raise StopPropagation
            # This needed for AFK to working properly

            except events.StopPropagation:
                raise events.StopPropagation
            # This is a gay exception and must be passed out. So that it doesnt
            # spam chats
            except KeyboardInterrupt:
                pass
            except BaseException:

                # Check if we have to disable it.
                # If not silence the log spam on the console,
                # with a dumb except.

                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**KING USERBOT ERROR REPORT**\n"
                    text += (
                        "Tidak ada yang dicatat kecuali fakta kesalahan dan tanggal\n\n"
                    )

                    ftext = "========== DISCLAIMER =========="
                    ftext += "\nFile ini HANYA diunggah di sini,"
                    ftext += "\nkami hanya mencatat fakta kesalahan dan tanggal,"
                    ftext += "\nkami menghormati privasi Anda,"
                    ftext += "\nAnda tidak boleh melaporkan kesalahan ini jika kamu sudah login group support"
                    ftext += "\ndata rahasia apa pun di sini, tidak ada yang mau lihat datamu\n"
                    ftext += "================================\n\n"
                    ftext += "--------BEGIN USERBOT TRACEBACK LOG--------\n"
                    ftext += "\nTanggal : " + date
                    ftext += "\nObrolan ID : " + str(check.chat_id)
                    ftext += "\nPengirim ID : " + str(check.sender_id)
                    ftext += "\n\nPemicu Acara :\n"
                    ftext += str(check.text)
                    ftext += "\n\nMelacak kembali info :\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text :\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = 'git log --pretty=format:"%an: %s" -10'

                    ftext += "\n\n\nLast 10 commits:\n"

                    process = await asyncsubshell(
                        command, stdout=asyncsub.PIPE, stderr=asyncsub.PIPE
                    )
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

                    ftext += result

                    with open("error.txt", "w+") as file:
                        file.write(ftext)

                    if LOGSPAMMER:
                        await check.respond(
                            "`Maaf , bot pengguna saya crashed.\
                        \nLog kesalahan disimpan di userbot obrolan log.`"
                        )

                        log = codecs.open("error.txt", "r", encoding="utf-8")
                        data = log.read()
                        key = (
                            requests.post(
                                "https://nekobin.com/api/documents",
                                json={"content": data},
                            )
                            .json()
                            .get("result")
                            .get("key")
                        )
                        url = f"https://nekobin.com/raw/{key}"
                        anu = f"{text}Pasted to: [Nekobin]({url})"

                        await check.client.send_file(send_to, "error.txt", caption=anu)
                        remove("error.txt")
            else:
                pass

        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator
