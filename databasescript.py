import sqlite3

# Connect to the database
conn = sqlite3.connect('players.db')
cursor = conn.cursor()

# Execute a query to get all data from the players table
cursor.execute("SELECT * FROM players")
rows = cursor.fetchall()

# Print out each row
for row in rows:
    print(row)

# Close the connection
conn.close()