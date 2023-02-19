import sqlite3
dbname='TEST2.db'
conn=sqlite3.connect(dbname)
cur=conn.cursor()

cur.execute('INSERT INTO person(name) values("Yamamoto")')
cur.execute('INSERT INTO person(name) values("Yamato")')
cur.execute('INSERT INTO person(name) values("Yamoto")')
conn.commit()
cur.execute('SELECT * FROM person')
for row in cur:
    return(row)
    
cur.close()
conn.close()