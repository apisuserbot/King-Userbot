import json
import urllib.request


from userbot.events import register
from userbot import CMD_HELP


# Port By @VckyouuBitch From GeezProject
# Buat Kamu Yang Hapus Credits. Intinya Kamu Anjing:)
# Recode Lynx-Userbot dari King-Userbot
# Dari Apis Terimakasih Vicky
@register(outgoing=True, pattern="^.ip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    king1 = result["type"]
    king2 = resut["country_code"]
    king3 = result["region_name"]
    king4 = result["city"]
    king5 = result["zip"]
    king6 = result["latitude"]
    king7 = result["longitude"]
    await event.edit(
        f"<b><u>INFORMASI BERHASIL DIKUMPULKAN</b></u>\n\n<b>Ip type :-</b><code>{king1}</code>\n<b>Country code:- </b> <code>{king2}</code>\n<b>State name :-</b><code>{king3}</code>\n<b>City name :- </b><code>{king4}</code>\n<b>zip :-</b><code>{king5}</code>\n<b>Latitude:- </b> <code>{king6}</code>\n<b>Longitude :- </b><code>{king7}</code>\n",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "fakeaddress": "**IP HACK**\
\n\n**Syntax : **`.ip <ip address>`\
\n**Usage :** Memberikan detail tentang alamat ip."
    }
)
