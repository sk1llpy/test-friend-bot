import sqlite3 as db

async def get_user(user_id):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    user = cur.execute(f"""SELECT * FROM user_test WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()

    return user


async def create_test(user_id, social, animal, place, season, weather, cake, month):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    cur.execute(f"""INSERT INTO user_test (user_id, so_media, animal, place_for_camp, season, weather, cake, month) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (str(user_id), social, animal, place, season, weather, cake, month))

    conn.commit()
    conn.close()
    
    
async def update_test(user_id, social, animal, place, season, weather, cake, month):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    cur.execute(f"""UPDATE user_test SET so_media = ?, animal = ?, place_for_camp = ?, season = ?, weather = ?, cake = ?, month = ? WHERE user_id = ? """, (social, animal, place, season, weather, cake, month, str(user_id)))

    conn.commit()
    conn.close()
    

async def add_result(user_id, name, from_user_id, from_name, result):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    cur.execute(f"""INSERT INTO result (user_id, fullname, from_user_id, from_fullname, result) VALUES (?, ?, ?, ?, ?)""", (str(user_id), name, str(from_user_id), from_name, result))

    conn.commit()
    conn.close()
    

async def get_result(user_id):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    user = cur.execute(f"""SELECT * FROM result WHERE user_id = {str(user_id)} ORDER BY result DESC""").fetchall()

    conn.commit()
    conn.close()

    return user


async def get_user_result(user_id):
    conn = db.connect('main.db')
    cur = conn.cursor()
    
    user = cur.execute(f"""SELECT * FROM result WHERE from_user_id = {str(user_id)} ORDER BY result DESC""").fetchall()

    conn.commit()
    conn.close()

    return user