import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')

# create table
con.execute("""
CREATE TABLE champs (
    id INTEGER PRIMARY KEY,
    name TEXT COLLATE NOCASE,
    championship TEXT COLLATE NOCASE,
    medal VARCHAR,
    event TEXT COLLATE NOCASE,
    time DATETIME,
    record TEXT COLLATE NOCASE )
""")

# insert values from old table (phelps) into new table (champs)
con.execute("""
INSERT INTO champs (name, championship, medal, event, time, record)
SELECT 'Michael Phelps', championship, medal, event, time, record
FROM phelps
""")

con.execute("DROP TABLE phelps")
