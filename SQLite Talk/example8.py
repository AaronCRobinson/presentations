import sqlite3, csv

data = []
with open('lochte.csv') as input:
    csvReader = csv.reader( input , 
        delimiter = ',', quotechar = '"')
    for row in csvReader:
        data.append(row)
data = data[1:] # skip header line

# create connection object
con = sqlite3.connect('db.sqlite')

insert = """
INSERT INTO champs (championship, name, medal, event, time, record)
VALUES (?,?,?,?,?,?)
"""

con.text_factory = str
con.executemany(insert, data)
con.commit()
