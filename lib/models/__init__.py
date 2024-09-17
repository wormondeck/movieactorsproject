import sqlite3

CONN = sqlite3.connect('movieactors.db')
CURSOR = CONN.cursor()
