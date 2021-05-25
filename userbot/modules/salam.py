from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern=r"^\.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern="^.Ass(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Halo salken saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum Waruhmatulahi Wabarukatuh`...")


@register(outgoing=True, pattern="^.Waa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**iyaa bro**")
    sleep(2)
    await typew.edit("`Walaikumsalam Waruhmatulahi Wabarukatuh`...")


@register(outgoing=True, pattern="^.L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


CMD_HELP.update(
    {
        "salam": "**✘ Plugin : **`salam`\
        \n\n  •  **Perintah :** `.P` `.p`\
        \n  •  **Function :** Untuk salam ke semua orang\
        \n\n  •  **Perintah :** `.Ass`\
        \n  •  **Function :** Salam kenal dan salam\
        \n\n  •  **Perintah :** `.Waa`\
        \n  •  **Function :** Menjawab salam panjang\
        \n\n  •  **Perintah :** `.L` `.l`\
        \n  •  **Function :** Untuk menjawab salam\
        \n\n\n  •  **Pesan untuk salam dan menjawab salam ke semua orang , dimanapun king berada.**\n**Pesan dari Apis , enjoy userbot:D**\
    "
    }
)
