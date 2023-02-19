import sqlite3
dbname='MyFavoriteHero.db'
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
cur=conn.cursor()
cur.execute('SELECT * FROM person')
for row in cur.fetchall():
    print(row["name"])
    print(row["voice"])
    print(row["speed"])
    print(row["type"])
conn.commit()
cur.close()
conn.close()