import sqlite3
dbname='TEST0.db'
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
cur=conn.cursor()
cur.execute('SELECT * FROM person')
for row in cur.fetchall():
    print(row["name"])
    #print(row["voice"])
    #print(row["speed"])
conn.commit()
cur.close()
conn.close()