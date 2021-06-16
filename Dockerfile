# KING USERBOT
FROM apiskinguserbot/kinguserbot:Buster

# Dockerfile
# KING
# Dockerfile
RUN git clone -b King-Userbot https://github.com/apisuserbot/King-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
