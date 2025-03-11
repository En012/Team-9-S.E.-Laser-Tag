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
            id SERIAL PRIMARY KEY,
            codename TEXT NOT NULL
        )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

#Checks if an entry is already in the database
#Returns true if it is. False if it is not
def checkInDatabase(id):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "SELECT 1 FROM players WHERE id = %s"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "SELECT 1 FROM players WHERE id = ?"
    
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    
    conn.close()
    return result is not None

def addPlayer(id, codename):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "INSERT INTO players (id, codename) VALUES (%s, %s)"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "INSERT INTO players (id, codename) VALUES (?, ?)"
    
    cursor.execute(query, (id, codename))
    conn.commit()    
    conn.close()

def removePlayer(id):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "DELETE FROM players WHERE id = %s"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "DELETE FROM players WHERE id = ?"
    
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()

def getCodeName(id):
    global insideVM

    if insideVM:
        conn = connectToVMDatabase()
        cursor = conn.cursor()
        query = "SELECT codename FROM players WHERE id = %s"
    else:
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
        query = "SELECT codename FROM players WHERE id = ?"

    cursor.execute(query, (id,))
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