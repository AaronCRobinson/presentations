import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')
con.text_factory = str

con.executescript("""
ALTER TABLE phelps RENAME TO junk;
CREATE TABLE phelps (
    championship VARCHAR(25),
    medal VARCHAR COLLATE NOCASE,
    event TEXT,
    time DATETIME,
    record CHARACTER(2) );
INSERT INTO phelps SELECT * FROM junk;
DROP TABLE junk;
""")

# lets count bronzes and silvers
select = """
SELECT count(*)
FROM phelps 
WHERE medal = 'SiLvEr' OR medal = 'Bronze'
"""
result = con.execute(select).fetchone()
print "The number of bronze and silvers Phelps received:", result[0]
