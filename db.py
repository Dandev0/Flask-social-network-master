import sqlite3
from flask import request, redirect

base = sqlite3.connect('db/sc.db', check_same_thread=False)
cur = base.cursor()

def avtorisation_login():
    r = cur.execute('SELECT LOGIN FROM data WHERE login ==?', (request.form.get('username'),)).fetchone()
    if r == None:
        return "Не корректный пароль"
    else:
        r = ','.join(map(str, r))
        return r

def avtorisation_password():
    c = cur.execute('SELECT PASSWORD FROM data WHERE password ==?', (request.form.get('password'),)).fetchone()
    if c == None:
        return "Не корректный пароль"
    else:
        c = ','.join(map(str, c))
        return c

def registration_user():
    reg = cur.execute('INSERT INTO data VALUES(?,?)', (request.form.get("regusername"),request.form.get("regpassword")))
    base.commit()
    return reg