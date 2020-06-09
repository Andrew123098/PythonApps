import sqlite3

##############
## BACK END ##
##############

## Connect to the database and connect/create the music table. 
def connect():
    conn=sqlite3.connect("music.db") # Connect to database file.
    cur=conn.cursor()                # Create cursor object to run through database.
    cur.execute("CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY, title text, artist text, album text, year integer)")
    conn.commit()                    # Commit changes to database.
    conn.close()                     # Close connection to database.

## Add song to music database
def insert(title, artist, album, year):
    conn=sqlite3.connect("music.db") # Connect to database file.
    cur=conn.cursor()                # Create cursor object to run through database.
    cur.execute("INSERT INTO music VALUES (NULL,?,?,?,?)", (title, artist, album, year))
    conn.commit()                    # Commit chnages to database.
    conn.close()                     # Close connection to database.

## View all songs in the music library.
def view():
    conn=sqlite3.connect("music.db")   # Connect to database file.
    cur=conn.cursor()                  # Create cursor object to run through database.
    cur.execute("SELECT * FROM music") # Select all data from music table in database.
    rows=cur.fetchall()                # Set variable to store all selected data.
    conn.close()                       # Close connection to database (no chnages made).
    return rows                        # Return all data from music table.

## Seach for a song using one or more of the 4 information entries.
def search(title="", artist="", album="", year=""): # Initialize variables to be empty strings.
    conn=sqlite3.connect("music.db")                # Connect to the database file.
    cur=conn.cursor()                               # Create cursor object to run through database.
    cur.execute("SELECT * FROM music WHERE title=? OR artist=? OR album=? OR year=?", (title, artist, album, year))
    rows=cur.fetchall()                             # Set variable to store all selected data.
    conn.close()                                    # Close connection to database (no chnages made).
    return rows                                     # Return all songs that match the search term.

## Delete a song from the music library.
def delete(id): 
    conn=sqlite3.connect("music.db") # Connect to the database file.
    cur=conn.cursor()                # Create cursor object to run through database.
    cur.execute("DELETE FROM music WHERE id=?", (id,))
    conn.commit()                    # Commit chnages to database.
    conn.close()                     # Close connection to database.

## Update a song in the music library.
def update(id,title,artist,album,year):
    conn=sqlite3.connect("music.db") # Connect to the database file.
    cur=conn.cursor()                # Create cursor object to run through database.
    cur.execute("UPDATE music SET title=?, artist=?, album=?, year=? WHERE id=?", (title, artist, album, year, id))
    conn.commit()                    # Commit chnages to database.
    conn.close()                     # Close connection to database.