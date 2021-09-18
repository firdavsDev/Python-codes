#youtubda codemy.com

from pathlib import Path #path kerak buladi
import sqlite3  #Import qilib olimiz

BASE_DIR = Path(__file__).parent / "sqllite_free.db" #fayl qayerda ochilishini kursatamiz


######################################## Baza yaratamiz
#conn=sqlite3.connect(:memory:)
conn=sqlite3.connect(BASE_DIR)

########################################### Bazaga table yaratmiz

#cursor yaratib olamiz
c=conn.cursor()

# NULL
# INTEGER
# REAL
# TEXT
# BLOB (media)

############################################################## Table yaratamiz

# c.execute(""" CREATE TABLE customers (
#         first_name text,
#         last_name tetx,
#         email text
    
#     )""")


############################################################## INSERT INTO MALUMOT QUSHISH


#Agar malumot kaupro bulsa 1-usul
# c.execute("INSERT INTO customers VALUES('Davron','Boltayev','xackercoder@gmail.com')")
# print('Bazaga qushildi')



#agar malumot kup bulsa. 2-usul
# many_customers=[
#     ('Davron','boltayev','email.@gmail.com'),
#     ('Firdavs','boltayev','email.@gmail.com'), #vergul ishlatiladi
#     ]
# c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)


############################################################## Query the database

# fetchall() fetchone() fetchmany() bazadag malumotlarni kursatish uchun
c.execute("SELECT rowid,* FROM customers")

#print(c.fetchall())
#print(c.fetchone()[0]) #index buyicha chiqorib beradi

items=c.fetchall()
for item in items:
    print(item)




#commit qilamiz bazamizni
conn.commit()


#close qilib yopamiz
conn.close()