from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern='^.Ass(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Halo bro saya {DEFAULTUSER} , salam kenal 😁`")
    sleep(3)
    await typew.edit("`Assalamualaikum Waruhmatulahi Wabarukatuh`...")


@register(outgoing=True, pattern='^.Waa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`iyaa bro..`")
    sleep(1)
    await typew.edit("`Walaikumsalam Waruhmatulahi Wabarukatuh`...")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam...`")


CMD_HELP.update(
    {
        "salam": "**✘ Plugin : **`salam`\
        \n\n  •  **Perintah :** `.p`\
        \n  •  **Function :** Untuk salam ke semua orang\
        \n\n  •  **Perintah :** `.Ass`\
        \n  •  **Function :** Salam kenal dan salam\
        \n\n  •  **Perintah :** `.Waa`\
        \n  •  **Function :** Menjawab salam panjang\
        \n\n  •  **Perintah :** `.l`\
        \n  •  **Function :** Untuk menjawab salam\
        \n\n\n  •  **Pesan : wajib menjawab pesan salam ke semua orang**\n**Pesan dari : Apis , enjoy userbot:D**\
    "
    }
)
