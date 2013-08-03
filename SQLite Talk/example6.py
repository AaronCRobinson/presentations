import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')
con.row_factory = sqlite3.Row
cur = con.cursor()

# sqlite_master stores the schema
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' and name='phelps'")

sql = cur.fetchone()['sql']

caseless = "TEXT COLLATE NOCASE"
sql = sql.replace("TEXT",caseless)
sql = sql.replace("VARCHAR(25)",caseless)
sql = sql.replace("CHARACTER(2)",caseless)
sql = sql.replace("VARCHAR", "TEXT")

cur.execute("PRAGMA writable_schema = 1")
cur.execute("UPDATE sqlite_master SET sql = ? WHERE type='table' and name='phelps'", (sql,))
cur.execute("PRAGMA writable_schema = 0")
