import sqlite3
import sys
id=sys.argv[2]
name=sys.argv[1]
voice=sys.argv[3]
speed=sys.argv[4]
type=sys.argv[5]
dbname='MyFavoriteHero.db'
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
cur=conn.cursor()
cur.execute('DELETE FROM person WHERE id=?',(id))
conn.commit()
cur.execute('INSERT INTO person(id,name,voice,speed,type) values(?,?,?,?,?);',(id,name,voice,speed,type))
conn.commit()
cur.execute('UPDATE person set id=?,name=?,voice=?,speed=?,type=? where id=?',(id,name,voice,speed,type,id))
conn.commit()
cur.close()
conn.close()