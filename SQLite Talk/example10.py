import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')
cur = con.cursor()

con.execute("""
CREATE VIEW report AS
SELECT c.id, c.name, c.championship, m.name AS medal, c.event, c.time, c.record
FROM champs AS c
JOIN medals AS m ON c.medal = m.id
""")

cur.execute("""
SELECT championship, event
FROM (SELECT championship, event, COUNT(*) AS cnt FROM champs GROUP BY championship, event)
WHERE cnt > 1
""")

s = "SELECT name,time,medal,record FROM report WHERE championship=? AND event=?"
for championship, event in cur:
    print "Championship:", championship
    print "Event:", event
    for row in con.execute(s, (championship, event) ):
        print "Name: %s\nTime:%s\tMedal:%s\tRecord:%s\n" % row
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        

