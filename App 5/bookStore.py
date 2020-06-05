# Andrew Brown : Last Edited 6/5/2020 
# The purpose of this program is to create a database table in postgresSQL that holds items in a store.
# Functions in this program allow me to manipulate the items in the database at will.

import psycopg2

def create_table():
    """ CREATE A TABLE IN A DATABASE FILE TO STORE DATA """
    conn=psycopg2.connect("""dbname='udemy_database1' user='postgres' password='postgres123'
    host='localhost' port='5432'""")                                                           # Connect to database
    cur=conn.cursor()                                                                          # Create cursor object
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")  # Create table to store data for store products 
    conn.commit()                                                                              # Commit chnages to database
    conn.close()                                                                               # Close connection to database

def insert(item,quantity,price):
    """ INSERT AN ITEM INTO THE DATABASE """
    conn=psycopg2.connect("""dbname='udemy_database1' user='postgres' password='postgres123'
    host='localhost' port='5432'""")                                                           # Connect to database
    cur=conn.cursor()                                                                          # Create cursor object
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))                  # Insert an item into store table in database
    conn.commit()                                                                              # Commit chnages to database
    conn.close()                                                                               # Close connection to database

def view():
    """ RETURN THE ENTIRE DATABASE """
    conn=psycopg2.connect("""dbname='udemy_database1' user='postgres' password='postgres123'
    host='localhost' port='5432'""")                                                           # Connect to database
    cur=conn.cursor()                                                                          # Create cursor object
    cur.execute("SELECT * FROM store")                                                         # Select table to get data from    
    rows=cur.fetchall()                                                                        # Save all table data in variable 
    conn.close()                                                                               # Close connection to database
    return rows                                                                                # Return data fetched from database

def delete(item):
    """ DELETE AN ITEM FROM THE DATABASE """
    conn=psycopg2.connect("""dbname='udemy_database1' user='postgres' password='postgres123'
    host='localhost' port='5432'""")                                                           # Connect to database
    cur=conn.cursor()                                                                          # Create cursor object
    cur.execute("DELETE FROM store WHERE item=%s",(item,))                                     # Delete item from the table
    conn.commit()                                                                              # Commit changes to the database
    conn.close()                                                                               # Close connection to database

def update(item,quantity,price):
    """ DELETE AN ITEM FROM THE DATABASE """
    conn=psycopg2.connect("""dbname='udemy_database1' user='postgres' password='postgres123'
    host='localhost' port='5432'""")                                                           # Connect to database
    cur=conn.cursor()                                                                          # Create cursor object
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))  # Update quantity and price of given item
    conn.commit()                                                                              # Commit changes to the database
    conn.close()                                                                               # Close connection to database
        

create_table()                                                                               

#insert("Wine Glass", 6, 49.95)
insert("Banana", 5, 1.20)

#print(view())

#update("Wine Glass", 6, 49.95/2)
#delete("Banana")

#print(view())