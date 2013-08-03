import sqlite3, csv

data = []
with open('phelps.csv') as input:
    csvReader = csv.reader( input , 
        delimiter = ',', quotechar = '"')
    for row in csvReader:
        data.append(row)
data = data[1:] # skip header line

# create connection object
con = sqlite3.connect('db.sqlite')

# create table
con.execute("""
CREATE TABLE phelps (
    championship VARCHAR(25),
    medal VARCHAR,
    event TEXT,
    time DATETIME,
    record CHARACTER(2) )
""")

con.text_factory = str
for row in data:
    con.execute( """INSERT INTO phelps
        VALUES (?,?,?,?,?)""", row)
con.commit()
