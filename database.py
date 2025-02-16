import sqlite3

#Initialize the database and create the players table if it doesn't exist.
def init_db():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team TEXT NOT NULL,
            player_number INTEGER,
            player_name TEXT,
            equipment_code TEXT
        )"""
    )
    conn.commit()
    conn.close()

#clears all records from the database
def cleardatabase():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players")
    conn.commit()
    conn.close()

#Saves players to the database, avoiding duplicates
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

#Returns the name of the player with the given ID
def get_player_name(player_id):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute("SELECT player_name FROM players WHERE equipment_code = ?", (player_id,))
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else None  # Return name if found, otherwise None

#Updates the player's name for the given player ID
def set_player_name(player_id, new_name):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE players SET player_name = ? WHERE equipment_code = ?", (new_name, player_id))
    conn.commit()
    conn.close()


#Checks if a given player ID exists; if not, adds it with 'None' as the name.
def check_or_add_player(player_id):
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()

    # Check if the player ID exists
    cursor.execute("SELECT * FROM players WHERE equipment_code = ?", (player_id,))
    result = cursor.fetchone()  # Fetch one matching row

    # Assign to "Unknown" team and default name "None"
    if result == None:
        cursor.execute(
            "INSERT INTO players (team, player_number, player_name, equipment_code) VALUES (?, ?, ?, ?)",
            ("Unknown", None, None, player_id)
        )
        conn.commit()

    conn.close()
    return result if result else None