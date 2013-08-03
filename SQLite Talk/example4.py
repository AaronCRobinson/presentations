import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')
con.row_factory = sqlite3.Row

select = """
SELECT event, MIN(time), MAX(time)
FROM phelps
GROUP BY event
"""

print "Below are min and max times for Phelp's grouped by race:"
for row in con.execute(select):
    print "Event:", row['event']
    print "Min:", row[1]
    print "Max:", row['MAX(time)']
    print
