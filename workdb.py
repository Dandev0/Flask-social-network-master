import sqlite3
from flask import request, redirect

base = sqlite3.connect('db/sc.db', check_same_thread=False)
cur = base.cursor()

r = cur.execute('SELECT*FROM data').fetchall()
print(r)