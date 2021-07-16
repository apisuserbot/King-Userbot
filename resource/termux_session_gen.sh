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
wget https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/resource/king-startup.py
pip install telethon
python king-startup.py

# ------------------------------------------------END-LOG---------------------------------------------------------- #
