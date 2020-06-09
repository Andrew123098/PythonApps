# Andrew Brown : Last Edited 6/9/2020
# This program stores song information:
# Title, Artist, Album, Year
#
# User Can:
# 
# View all records
# Search an entry
# Add an entry
# Update an entry
# Delete an entry
# Clear all entries
#
# NOTE: To create a .exe file, use the termial command 'pyinstaller --onefile --windowed frontend.py'

##################
## BACK END OOP ##
##################

import sqlite3

class Database:

    ## Connect to the database and connect/create the music table. 
    def __init__(self, db):                   # Executed everytime the class is called.
        self.conn=sqlite3.connect("music.db") # Connect to database file.
        self.cur=self.conn.cursor()           # Create cursor object to run through database.
        self.cur.execute("CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY, title text, artist text, album text, year integer)")
        self.conn.commit()                    # Commit changes to database.

    ## Add song to music database
    def insert(self, title, artist, album, year):
        self.cur.execute("INSERT INTO music VALUES (NULL,?,?,?,?)", (title, artist, album, year))
        self.conn.commit()                    # Commit changes to database.

    ## View all songs in the music library.
    def view(self):
        self.cur.execute("SELECT * FROM music") # Select all data from music table in database.
        rows=self.cur.fetchall()                # Set variable to store all selected data.
        return rows                             # Return all data from music table.

    ## Seach for a song using one or more of the 4 information entries.
    def search(self, title="", artist="", album="", year=""): # Initialize variables to be empty strings.
        self.cur.execute("SELECT * FROM music WHERE title=? OR artist=? OR album=? OR year=?", (title, artist, album, year))
        rows=self.cur.fetchall()                              # Set variable to store all selected data.
        return rows                                           # Return all songs that match the search term.

    ## Delete a song from the music library.
    def delete(self, id): 
        self.cur.execute("DELETE FROM music WHERE id=?", (id,))
        self.conn.commit()  # Commit changes to database.

    ## Update a song in the music library.
    def update(self, id,title,artist,album,year):
        self.cur.execute("UPDATE music SET title=?, artist=?, album=?, year=? WHERE id=?", (title, artist, album, year, id))
        self.conn.commit()  # Commit changes to database.

    ## Exit the script and close the connection to the database
    def __del__(self):
        self.conn.close()