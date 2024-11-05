import sqlite3 as sq
with sq.connect('usersInfo.db') as con:
    cur = con.cursor()

    sql = """DELETE FROM users"""

    cur.execute(sql)
    con.commit()