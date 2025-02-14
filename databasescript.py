import sqlite3

#connecting to the database
conn = sqlite3.connect('players.db')
cursor = conn.cursor()

#execute a query to get all data from the players table
cursor.execute("SELECT * FROM players")
rows = cursor.fetchall()

#print out each row
for row in rows:
    print(row)

#close the connection
conn.close()