import sqlite3

peopleValues = (
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat popsicle', 100),
    ("Ak'Not", 'Mangalore', -5)
    )

with sqlite3.connect('tet_databases.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Rosters")
    c.execute("CREATE TABLE Rosters(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Rosters VALUES(?, ?, ?)", peopleValues)
    c.execute("UPDATE Rosters SET Species=? WHERE Name=?",
              ('Human', 'Korben Dallas'))
    c.execute("SELECT Name, IQ FROM Rosters WHERE Species == 'Human'")



for row in c.fetchall():
    print(row)
    
