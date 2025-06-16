import sqlite3

# Connect to roster.db
conn = sqlite3.connect('roster.db')
cur = conn.cursor()

# Create Roster table
cur.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Insert data
cur.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Update Jadzia Dax to Ezri Dax
cur.execute('UPDATE Roster SET Name = ? WHERE Name = ?', ('Ezri Dax', 'Jadzia Dax'))

# Query: Name and Age where Species is Bajoran
print("Bajoran Characters:")
for row in cur.execute('SELECT Name, Age FROM Roster WHERE Species = "Bajoran"'):
    print(row)

# Delete characters older than 100
cur.execute('DELETE FROM Roster WHERE Age > 100')

# Add Rank column
cur.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')

# Update ranks
ranks = {
    'Benjamin Sisko': 'Captain',
    'Ezri Dax': 'Lieutenant',
    'Kira Nerys': 'Major'
}
for name, rank in ranks.items():
    cur.execute('UPDATE Roster SET Rank = ? WHERE Name = ?', (rank, name))

# Advanced Query: Sort by Age descending
print("\nCharacters sorted by Age (descending):")
for row in cur.execute('SELECT Name, Species, Age, Rank FROM Roster ORDER BY Age DESC'):
    print(row)

conn.commit()
conn.close()
