import sqlite3

#Initialize the database and create the players table if it doesn't exist.
def initialize_database():
    # Connect to the SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    
    # Create the Players table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Players (
            playerID INTEGER PRIMARY KEY,
            codeName TEXT NOT NULL
        )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

#Checks if an entry is already in the database
#Returns true if it is. False if it is not
def checkInDatabase(playerID):
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT 1 FROM Players WHERE playerID = ?", (playerID,))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

#Adds an entry with the given playerID and codename to the database
def addPlayer(playerID, codename):
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO Players (playerID, Codename) VALUES (?, ?)", (playerID, codename))
        conn.commit()
        print("Player added successfully.")
    except sqlite3.IntegrityError:
        print("Error: PlayerID already exists.")
    
    conn.close()

#Removes the player with the specified ID from the database
def removePlayer(playerID):
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM Players WHERE playerID = ?", (playerID,))
    conn.commit()
    conn.close()
    print("Player removed successfully.")

def getCodeName(playerID):
    conn = sqlite3.connect("players.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT Codename FROM Players WHERE playerID = ?", (playerID,))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else None