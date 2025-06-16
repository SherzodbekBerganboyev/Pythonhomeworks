import sqlite3
conn = sqlite3.connect('library.db')
cur = conn.cursor()

# Create Books table
cur.execute('''
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
''')

# Insert data
cur.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
])

# Update Year_Published of 1984
cur.execute('UPDATE Books SET Year_Published = 1950 WHERE Title = "1984"')

# Query: Title and Author where Genre is Dystopian
print("\nDystopian Books:")
for row in cur.execute('SELECT Title, Author FROM Books WHERE Genre = "Dystopian"'):
    print(row)

# Delete books published before 1950
cur.execute('DELETE FROM Books WHERE Year_Published < 1950')

# Add Rating column
cur.execute('ALTER TABLE Books ADD COLUMN Rating REAL')

# Update ratings
ratings = {
    'To Kill a Mockingbird': 4.8,
    '1984': 4.7,
    'The Great Gatsby': 4.5  # This will be ignored as it's deleted
}
for title, rating in ratings.items():
    cur.execute('UPDATE Books SET Rating = ? WHERE Title = ?', (rating, title))

# Advanced Query: Sort by Year_Published ascending
print("\nBooks sorted by Year_Published (ascending):")
for row in cur.execute('SELECT Title, Author, Year_Published, Rating FROM Books ORDER BY Year_Published ASC'):
    print(row)

conn.commit()
conn.close()
