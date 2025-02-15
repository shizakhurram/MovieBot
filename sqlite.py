import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# Create the MOVIES table
table_info = """
CREATE TABLE IF NOT EXISTS MOVIES (
    TITLE TEXT,
    GENRE TEXT,
    RATING FLOAT
);
"""
cursor.execute(table_info)

# Insert movie records (Sample Data)
movies_data = [
    ("Inception", "Sci-Fi", 8.8),
    ("Interstellar", "Sci-Fi", 8.6),
    ("The Godfather", "Crime", 9.2),
    ("The Dark Knight", "Action", 9.0),
    ("Forrest Gump", "Drama", 8.8),
    ("The Matrix", "Sci-Fi", 8.7),
    ("Titanic", "Romance", 7.8),
    ("Joker", "Drama", 8.4),
    ("Avengers: Endgame", "Action", 8.4),
    ("Pulp Fiction", "Crime", 8.9)
]

# Insert movies into the database
cursor.executemany("INSERT INTO MOVIES (TITLE, GENRE, RATING) VALUES (?, ?, ?)", movies_data)

# Commit changes and close connection
connection.commit()
connection.close()

print("Movie database created successfully!")
