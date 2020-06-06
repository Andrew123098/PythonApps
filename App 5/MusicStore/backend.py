import sqlite3

def connect():
    conn=sqlite3.connect("music.db")
    cur=conncursor()
    cur.execute("CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY, title text, artist text, album text, year integer")
    conn.commit()
    conn.close()

def insert(title, artist, album, year):
    conn=sqlite3.connect("music.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO music VALUES (NULL,?,?,?,?)", (title, artist, album, year))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("music.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM music")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", artist="", album="", year=""):
    conn=sqlite3.connect("music.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM music WHERE title=? OR artist=? OR album=? OR year=?", (title, artist, album, year))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("music.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM music WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,artist,album,year):
    conn=sqlite3.connect("music.db")
    cur=conn.cursor()
    cur.execute("UPDATE music SET title=?, artist=?, album=?, year=? WHERE id=?", (title, artist, album, year, id))
    conn.commit()
    conn.close()