import os
import sqlite3
import psycopg2

#global variable, used to keep track of if the user is inside the Virtual Machine or not
#true = user is in VM, false = user is not in VM
insideVM = True

#initalize the database, called in main.py
def initialize_database():
    global insideVM

    #check if the operating system is linux
    if os.name == "posix":
        
        try:
            # Try connecting to the PostgreSQL database
            conn = connectToVMDatabase()
            cursor = conn.cursor()
        except Exception as e:
            print(f"PostgreSQL connection failed: {e}\nFalling back to SQLite.")
            insideVM = False
 
        # Fallback to SQLite
        conn = sqlite3.connect("players.db")
        cursor = conn.cursor()
    #if operating system is not linux, just go straight to sqlite
    else:
        insideVM = False
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

#Checks if an entry is already in the database
#Returns true if it is. False if it is not
def checkInDatabase(id):
    global insideVM

    #run a different SQL command depending on if the user is in the VM or not
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

#Adds an entry with the given playerID and codename to the database
def addPlayer(id, codename):
    global insideVM

    #run a different SQL command depending on if the user is in the VM or not
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

#Removes the player with the specified ID from the database
def removePlayer(id):
    global insideVM

    #run a different SQL command depending on if the user is in the VM or not
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

#Retrieves the codename associated with the given playerID as a string, returns None if player id is not found
def getCodeName(id):
    global insideVM

    #run a different SQL command depending on if the user is in the VM or not
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

#used to connect to the database inside the VM
#only runs if insideVM = true
def connectToVMDatabase():
    conn = psycopg2.connect(
            dbname="photon",
            user="student",
            password="student",
            host="localhost",
            port="5432"
        )
    return conn