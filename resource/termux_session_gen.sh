# ------------------------------------------------DEPLOYING-TERMUX------------------------------------------------------------>
clear
echo "
██╗░░██╗██╗███╗░░██╗░██████╗░
██║░██╔╝██║████╗░██║██╔════╝░
█████═╝░██║██╔██╗██║██║░░██╗░
██╔═██╗░██║██║╚████║██║░░╚██╗
██║░╚██╗██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
"
# Start deploying...
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/resource/userbot
pip3 install telethon
python3 -m userbot

# ------------------------------------------------END-LOG---------------------------------------------------------- #
