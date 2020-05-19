import mysql.connector

# Establish connection to database
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# Cursor object used to navigte through the table in the databse
cursor = con.cursor()

# Take input word from the user
word = input("Enter a word: ")

# We need to query some data from the database
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

print(type(results))
if results:                  # If the word is a real word (if it exists in the database
    print(results[1])        # Print only the first item in the list
else:                        # Otherwise
    print("No word found")   # Print that the word is wrong
