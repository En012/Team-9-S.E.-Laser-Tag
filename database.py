import sqlite3

def init_db():
    
    #Initialize the database and create the players table if it doesn't exist.
    
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team TEXT NOT NULL,
            player_number INTEGER,
            player_name TEXT,
            equipment_code TEXT
        )
    ''')
    conn.commit()
    conn.close()

#function for clearing data base (mainly using for testing at the moment)
def cleardatabase():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players")
    conn.commit()
    conn.close()

#main function to save players, intention is to ignore duplicate additions.
def save_players(team, names, equipment_codes):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    for i, (name, eq) in enumerate(zip(names, equipment_codes), start=1):
        if name.strip():
            cursor.execute(
                "SELECT COUNT(*) FROM players WHERE team = ? AND player_number = ?",
                (team, i)
            )
            if cursor.fetchone()[0] == 0:  # Only insert if no existing record
                cursor.execute(
                    "INSERT INTO players (team, player_number, player_name, equipment_code) VALUES (?, ?, ?, ?)",
                    (team, i, name.strip(), eq.strip())
                )

    conn.commit()
    conn.close()