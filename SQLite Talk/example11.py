import sqlite3, zlib, glob, os

# create connection object
con = sqlite3.connect('db.sqlite')
con.row_factory = sqlite3.Row

# create table
con.execute("CREATE TABLE code (id INT PRIMARY KEY, filename TEXT, data BLOB)")

def compressFile(infile):
    with open(infile) as f:
        name = os.path.basename(infile)
        compressed_data = sqlite3.Binary(zlib.compress(f.read()))
    return (name, compressed_data)

for f in glob.glob('*.py'):
    con.execute("INSERT INTO code ('filename','data') VALUES(?,?)", compressFile(f))
con.commit()

for row in con.execute("SELECT * FROM code"):
    print "Filename:", row['filename']
    print "Compressed data lenght:", len(row['data'])
    decompress = zlib.decompress(row['data'])
    print "Decompressed data lenght:", len(decompress)
    print
