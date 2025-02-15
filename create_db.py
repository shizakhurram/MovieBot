import sqlite3

# Connect to SQLite database (creates the file if not exists)
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# Create the MOVIES table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MOVIES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TITLE TEXT NOT NULL,
        GENRE TEXT NOT NULL,
        RATING REAL NOT NULL
    )
''')

# Insert sample movies
movies_data = [
    ("The Godfather", "Drama", 9.2),
    ("Titanic", "Romance", 7.8),
    ("Inception", "Sci-Fi", 8.8),
    ("Forrest Gump", "Drama", 8.8),
    ("Pulp Fiction", "Crime", 8.9),
    ("The Dark Knight", "Action", 9.0),
    ("The Notebook", "Romance", 7.9),
    ("Interstellar", "Sci-Fi", 8.6),
    ("Joker", "Drama", 8.4),
    ("Avengers: Endgame", "Action", 8.4)
]

# Insert data into the MOVIES table
cursor.executemany("INSERT INTO MOVIES (TITLE, GENRE, RATING) VALUES (?, ?, ?)", movies_data)

# Commit and close
connection.commit()
connection.close()

print("Database created successfully with movie data!")
