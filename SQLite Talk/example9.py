import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')
con.row_factory = sqlite3.Row

con.execute("""
CREATE TABLE medals (
    id INTEGER PRIMARY KEY,
    name TEXT)
""")
# make name case insensitive unique
con.execute("CREATE UNIQUE INDEX uidxName ON medals (name COLLATE NOCASE)")

datafix = [ (3,'Gold'), (2,'Silver'), (1,'Bronze') ]
con.executemany("INSERT INTO medals VALUES (?,?)", datafix)
con.executemany("UPDATE champs SET medal = ? WHERE medal = ?", datafix)

where_clause = "WHERE type='table' and name='champs'"
sql = con.execute("SELECT sql FROM sqlite_master " + where_clause).fetchone()['sql']
sql = sql.replace("medal TEXT COLLATE NOCASE,","medal INTEGER")

con.execute("PRAGMA writable_schema = 1")
con.execute("UPDATE sqlite_master SET sql = ? " + where_clause, (sql,))
con.execute("PRAGMA writable_schema = 0")
