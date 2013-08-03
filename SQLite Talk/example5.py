import sqlite3

# create connection object
con = sqlite3.connect('db.sqlite')
con.row_factory = sqlite3.Row

cur = con.cursor()

# sqlite_master stores the schema
cur.execute("SELECT * FROM sqlite_master")

# description is a 7-tuple w/ [Nones]*6
headers = zip(*cur.description)[0]

# print out data in sqlite_master
for record in cur:
    print "New Record:"
    for field in headers:
        print "%s: %s" %(field, record[field])
