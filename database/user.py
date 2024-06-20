import sqlite3 as db


async def get_user(user_id):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    user = cur.execute(f"""SELECT * FROM users WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()

    return user


async def add_user(user_id, username, name):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    cur.execute(f"""INSERT INTO users (user_id, username, fullname) VALUES (?, ?, ?)""", (str(user_id), f'@{username}', name))

    conn.commit()
    conn.close()