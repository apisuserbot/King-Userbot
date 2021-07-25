# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
from os import remove
from sys import executable

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, TERM_ALIAS
from userbot.events import register


@register(outgoing=True, pattern=r"^\.eval(?: |$)(.*)")
async def evaluate(query):
    if query.is_channel and not query.is_group:
        return await query.edit("`Eval isn't permitted on channels`")

    if query.pattern_match.group(1):
        expression = query.pattern_match.group(1)
    else:
        return await query.edit("`Berikan ekspresi untuk dievaluasi`")

    if expression in ("userbot.session", "config.env"):
        return await query.edit("`Itu evaluasi yang berbahaya! Tidak diperbolehkan!`")

    try:
        evaluation = str(eval(expression))
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open("output.txt", "w+")
                    file.write(evaluation)
                    file.close()
                    await query.client.send_file(
                        query.chat_id,
                        "output.txt",
                        reply_to=query.id,
                        caption="`Output terlalu besar, mengirim sebagai file`",
                    )
                    remove("output.txt")
                    return
                await query.edit(
                    "**Query : **\n`"
                    f"{expression}"
                    "`\n**Result : **\n`"
                    f"{evaluation}"
                    "`"
                )
        else:
            await query.edit(
                "**Query : **\n`"
                f"{expression}"
                "`\n**Result : **\n`Tidak Ada Hasil yang Dikembalikan/Salah`"
            )
    except Exception as err:
        await query.edit(
            "**Query : **\n`" f"{expression}" "`\n**Exception : **\n" f"`{err}`"
        )

    if BOTLOG:
        await query.client.send_message(
            BOTLOG_CHATID, f"Kueri evaluasi {expression} sukses dieksekusi"
        )


@register(outgoing=True, pattern=r"^\.exec(?: |$)([\s\S]*)")
async def run(run_q):
    code = run_q.pattern_match.group(1)

    if run_q.is_channel and not run_q.is_group:
        return await run_q.edit("`Exec tidak diizinkan di saluran!`")

    if not code:
        return await run_q.edit(
            "```Setidaknya variabel diperlukan untuk"
            "execute Menggunakan help exec untuk contoh```"
        )

    if code in ("userbot.session", "config.env"):
        return await run_q.edit("`Itu exec yang berbahaya! Tidak diperbolehkan!`")

    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = (
            clines[0] +
            "\n" +
            clines[1] +
            "\n" +
            clines[2] +
            "\n" +
            clines[3] +
            "...")

    command = "".join(f"\n {l}" from l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        executable,
        "-c",
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if result:
        if len(result) > 4096:
            file = open("output.txt", "w+")
            file.write(result)
            file.close()
            await run_q.client.send_file(
                run_q.chat_id,
                "output.txt",
                reply_to=run_q.id,
                caption="`Output too large, sending as file`",
            )
            remove("output.txt")
            return
        await run_q.edit(
            "**Query : **\n`" f"{codepre}" "`\n**Result : **\n`" f"{result}" "`"
        )
    else:
        await run_q.edit(
            "**Query : **\n`" f"{codepre}" "`\n**Result : **\n`Tidak Ada Hasil yang Dikembalikan/Salah`"
        )

    if BOTLOG:
        await run_q.client.send_message(
            BOTLOG_CHATID, "kueri exec " + codepre + " sukses dieksekusi"
        )


@register(outgoing=True, pattern=r"^\.term(?: |$)(.*)")
async def terminal_runner(term):
    curruser = TERM_ALIAS
    command = term.pattern_match.group(1)
    try:
        from os import geteuid

        uid = geteuid()
    except ImportError:
        uid = "Ini bukan kepala!"

    if term.is_channel and not term.is_group:
        return await term.edit("`Perintah istilah tidak diizinkan di saluran!`")

    if not command:
        return await term.edit(
            "```Berikan perintah atau gunakan .help term untuk contoh```"
        )

    if command in ("userbot.session", "config.env"):
        return await term.edit("`Itu term yang berbahaya! Tidak diperbolehkan!`")

    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await term.client.send_file(
            term.chat_id,
            "output.txt",
            reply_to=term.id,
            caption="`Output terlalu besar, mengirim sebagai file`",
        )
        remove("output.txt")
        return

    if uid == 0:
        await term.edit("`" f"{curruser} :~# {command}" f"\n{result}" "`")
    else:
        await term.edit("`" f"{curruser} :~$ {command}" f"\n{result}" "`")


"""
    if BOTLOG:
        await term.client.send_message(
            BOTLOG_CHATID,
            "Terminal Perintah " + command + " sukses dieksekusi",
        )
"""

CMD_HELP.update(
    {"eval": "**✘ Plugin :** `Eval Teks`\
        \n\n  •  **Perintah :** `.eval` 2 + 3\
        \n  •  **Function : Evaluasi ekspresi mini\
    "
     }
)

CMD_HELP.update(
    {
        "exec": "**✘ Plugin :** `Exec Teks`\
        \n\n  •  **Perintah :** `.exec` `print('hello')`\
        \n  •  **Function : **Jalankan skript python kecil\
    "
    }
)

CMD_HELP.update(
    {
        "term": "**✘ Plugin :** `Term Teks`\
        \n\n  •  **Perintah :** `.term` <cmd>\
        \n  •  **Function : **Jalankan perintah dan skript bash di server Anda\
    "
    }
)
