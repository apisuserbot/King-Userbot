from userbot.modules.sql_helper import SESSION

try:
    eval(SESSION.get("ECHO"))
except BaseException:
    SESSION.get("ECHO", "{}")


def add_echo(chat, user):
    x = eval(SESSION.get("ECHO"))
    try:
        k = x[chat]
        if user not in k:
            k.append(user)
        x.update({chat: k})
    except BaseException:
        x.update({chat: [user]})
    return SESSION.get("ECHO", str(x))


def rem_echo(chat, user):
    x = eval(SESSION.get("ECHO"))
    try:
        k = x[chat]
        if user in k:
            k.remove(user)
        x.update({chat: k})
    except BaseException:
        pass
    return SESSION.get("ECHO", str(x))


def check_echo(chat, user):
    x = eval(SESSION.get("ECHO"))
    try:
        k = x[chat]
        if user in k:
            return True
        return
    except BaseException:
        return


def list_echo(chat):
    x = eval(SESSION.get("ECHO"))
    try:
        k = x[chat]
        return k
    except BaseException:
        return
