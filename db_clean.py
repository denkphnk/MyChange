import sqlite3 as sq
with sq.connect('data/usersInfo.db') as con:
    cur = con.cursor()

    sql = """DELETE FROM users"""

    cur.execute(sql)

    sql = """DELETE FROM targets"""

    cur.execute(sql)

    con.commit()