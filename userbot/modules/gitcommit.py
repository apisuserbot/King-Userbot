# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Ported to UserBot by @Mayur_Karaniya

from github import Github
import os
import time
from datetime import datetime

# from sample_config import Config
# from uniborg.util import admin_cmd, humanbytes, progress, time_formatter
from userbot.events import register

# from userbot.events import humanbytes, progress, time_formatter
from userbot import CMD_HELP, GITHUB_ACCESS_TOKEN, GIT_REPO_NAME, bot


GIT_TEMP_DIR = "./userbot/temp/"
# @borg.on(admin_cmd(pattern="commit ?(.*)", allow_sudo=True))


@register(outgoing=True, pattern=r"^\.gcommit(?: |$)(.*)")
# @register(pattern=r".commit (.*)", outgoing=True)
async def download(event):
    if event.fwd_from:
        return
    if GITHUB_ACCESS_TOKEN is None:
        await event.edit("`Please ADD Proper Access Token from github.com`")
        return
    if GIT_REPO_NAME is None:
        await event.edit("`Please ADD Proper Github Repo Name of your userbot`")
        return
    mone = await event.reply("Processing ...")
    if not os.path.isdir(GIT_TEMP_DIR):
        os.makedirs(GIT_TEMP_DIR)
    start = datetime.now()
    reply_message = await event.get_reply_message()
    try:
        time.time()
        print("Downloading to TEMP directory")
        downloaded_file_name = await bot.download_media(
            reply_message.media, GIT_TEMP_DIR
        )
    except Exception as e:
        await mone.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await mone.edit(
            "Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms)
        )
        await mone.edit("Committing to Github....")
        await git_commit(downloaded_file_name, mone)


async def git_commit(file_name, mone):
    content_list = []
    access_token = GITHUB_ACCESS_TOKEN
    g = Github(access_token)
    file = open(file_name, "r", encoding="utf-8")
    commit_data = file.read()
    repo = g.get_repo(GIT_REPO_NAME)
    print(repo.name)
    create_file = True
    contents = repo.get_contents("")
    for content_file in contents:
        content_list.append(str(content_file))
        print(content_file)
    for i in content_list:
        create_file = True
        if i == 'ContentFile(path="' + file_name + '")':
            return await mone.edit("`File Already Exists`")
            create_file = False
    file_name = "userbot/modules/" + file_name
    if create_file:
        file_name = file_name.replace("./userbot/temp/", "")
        print(file_name)
        try:
            repo.create_file(
                file_name, "Uploaded New Plugin", commit_data, branch="King-Userbot"
            )
            print("Committed File")
            ccess = GIT_REPO_NAME
            ccess = ccess.strip()
            await mone.edit(
                f"`Commited On Your Github Repo`\n\n[Your Plugins](https://github.com/{ccess}/tree/King-Userbot/userbot/modules/)"
            )
        except BaseException:
            print("Cannot Create Plugin")
            await mone.edit("Cannot Upload Plugin")
    else:
        return await mone.edit("`Committed Suicide`")


CMD_HELP.update(
    {
        "gcommit": "**✘ Plugin :** `gcommit`\
        \n\n  •  **Perintah :** `.gcommit`\
        \n  •  **Function : **GITHUB File Uploader Plugin for userbot. Heroku Automation should be Enabled. Else u r not that lazy , For lazy people\
        \n\n  •  **Instructions :- **Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in Heroku vars First\
        \n  commit reply_to_any_plugin can be any type of file too. but for plugin must be in .py\
    "
    }
)
