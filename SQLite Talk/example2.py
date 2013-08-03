import sqlite3 

# create connection object
con = sqlite3.connect('db.sqlite')
con.text_factory = str

from_where = """
FROM phelps
WHERE medal = 'Gold'
"""

# lets count how many golds phelp has
select = "SELECT count(*)" + from_where
result = con.execute(select).fetchone()
golds = int(result[0])
print "The number of golds Michael Phelp's has won in his olympic career is: %i" % golds
print type(result) # returns a tuple

# lets see the events (NOTE: duplicates)
print "The events Phelps was in:"
select = "SELECT event" + from_where
for rec in con.execute(select):
    print rec[0]
