# Docker Tag Images, Using Python Slim Buster 3.9
FROM apiskinguserbot/kinguserbot:Buster
# ==========================================
#              USERBOT TELEGRAM
# ==========================================
RUN git clone -b King-Userbot https://github.com/apisuserbot/King-Userbot /home/King-Userbot \
    && chmod 777 /home/King-Userbot \
    && mkdir /home/King-Userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/King-Userbot/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/requirements.txt
WORKDIR /home/King-Userbot/

# Finishim
CMD ["python3","-m","userbot"]
