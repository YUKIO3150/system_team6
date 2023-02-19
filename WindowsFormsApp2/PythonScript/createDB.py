# -*- coding: utf-8 -*-
import sqlite3
 
con = sqlite3.connect('MyFavoriteHero.db')
cur = con.cursor() 
cur.execute("CREATE TABLE person(id integer PRIMARY KEY,name text,voice integer,speed real,type integer)")
con.commit()
con.close()