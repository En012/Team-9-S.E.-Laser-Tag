import sqlite3
import psycopg2

insideVM = True
def initialize_database():
    try:
        # Try connecting to the PostgreSQL database
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        print("Connected to PostgreSQL database.")
    except Exception as e:
        print(f"PostgreSQL connection failed: {e}\nFalling back to SQLite.")
        global insideVM
        insideVM = False
        
        # Fallback to SQLite
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
    
    # Create the Players table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            playerID SERIAL PRIMARY KEY,
            codeName TEXT NOT NULL
        )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

#Checks if an entry is already in the database
#Returns true if it is. False if it is not
def checkInDatabase(playerID):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "SELECT 1 FROM players WHERE playerID = %s"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "SELECT 1 FROM players WHERE playerID = ?"
    
    cursor.execute(query, (playerID,))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

def addPlayer(playerID, codename):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "INSERT INTO players (playerID, codeName) VALUES (%s, %s)"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "INSERT INTO players (playerID, codeName) VALUES (?, ?)"
    
    cursor.execute(query, (playerID, codename))
    conn.commit()    
    conn.close()

def removePlayer(playerID):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "DELETE FROM players WHERE playerID = %s"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "DELETE FROM players WHERE playerID = ?"
    
    cursor.execute(query, (playerID,))
    conn.commit()
    conn.close()

def getCodeName(playerID):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "SELECT codeName FROM players WHERE playerID = %s"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "SELECT codeName FROM players WHERE playerID = ?"

    cursor.execute(query, (playerID,))
    result = cursor.fetchone()
    
    conn.close()
    return result[0] if result else None

def connectToVMDatabase():
    conn = psycopg2.connect(
            dbname="photon",
            user="student",
            password="student",
            host="localhost",
            port="5432"
        )
    return conn