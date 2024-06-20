import sqlite3 as db


async def create_table():
    conn = db.connect('main.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(255),
    username VARCHAR(255),
    fullname VARCHAR(255)
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS user_test (
    user_id VARCHAR(255),
    so_media VARCHAR(255),
    animal VARCHAR(255),
    place_for_camp VARCHAR(255),
    season VARCHAR(255),
    weather VARCHAR(255),
    cake VARCHAR(255),
    month VARCHAR(255)
    )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS result (
    user_id VARCHAR(255),
    fullname VARCHAR(255),
    from_user_id VARCHAR(255),
    from_fullname VARCHAR(255),
    result VARCHAR(255)
    )""")
    
    conn.commit()
    conn.close()