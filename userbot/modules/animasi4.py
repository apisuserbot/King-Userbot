# Ported by Apis (King-Userbot)
# animasi 4 file

import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.bacot(?: |$)(.*)")
async def bacot(event):
    await event.edit("**BACOT LUUU**")


@register(outgoing=True, pattern="^.sokap(?: |$)(.*)")
async def sokap(event):
    await event.edit("**SOKAP BAT JADI ORANG YA ANJING**")


@register(outgoing=True, pattern="^.woi(?: |$)(.*)")
async def woi(event):
    await event.edit("**WOI LU SEMUA**")


@register(outgoing=True, pattern="^.ngatur(?: |$)(.*)")
async def ngatur(event):
    await event.edit("**WOI ANJING , DENGER YA , JADI ORANG GAK USAH NGATUR NGATUR HIDUP ORANG YA NGENTOT , URUS AJA HIDUP LU SENDIRI BANGSAT , UDAH BENER APA KAGAK**")


@register(outgoing=True, pattern="^.berantem(?: |$)(.*)")
async def berantem(event):
    await event.edit("**WOI ANJING**")
    sleep(3)
    await event.edit("**BERANTEM YO NGENTOT**")
    sleep(3)
    await event.edit("**JANGAN JADI BANCI KETAKUTAN YA ANJING , SHARE LOCK SEKARANG BANGSAT**")
    sleep(5)
    await event.edit("**JANGAN MENTAL SOSMED DOANG LU**")


@register(outgoing=True, pattern="^.rp(?: |$)(.*)")
async def rp(event):
    await event.edit("**WOI ANAK RP NGENTOT , DENGER NI YA , PLASTIK MAH UDAH PLASTIK AJA**")
    sleep(3)
    await event.edit("**GOBLOK KOK DI RAWAT , UDAH NYEMBAH PLASTIK SAMPAH LAGI HAHAHAHA**")
    sleep(3)
    await event.edit("**MAKAN TUH PLASTIK AWOKAWOKAWOK**")


CMD_HELP.update(
    {
        "roasting": "**✘ Plugin :** `Roasting`\
        \n\n  •  **Perintah :** `.bacot`\
        \n  •  **Function : **Animasi Bacot\
        \n\n  •  **Perintah :** `.sokap`\
        \n  •  **Function : **Animasi Sokap\
        \n\n  •  **Perintah :** `.woi`\
        \n  •  **Function : **Animasi Woi\
        \n\n  •  **Perintah :** `.ngatur`\
        \n  •  **Function : **Animasi Ngatur\
        \n\n  •  **Perintah :** `.berantem`\
        \n  •  **Function : **Animasi Berantem\
        \n\n  •  **Perintah :** `.rp`\
        \n  •  **Function : **Animasi rp\
    "
    }
)
