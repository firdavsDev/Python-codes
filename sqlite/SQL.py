#Import qilamiz bazani
import sqlite3

#YouTube @WebDevPro

#####################333333333333333333333333333333333333333333##### 1 DARSDA baza yasab olish #####################################################################

# try:
#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ismi.db')

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#     sql='select sqlite_version();'
#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)

#     result=cursor.fetchall()
#     print('versiyasi',result)

#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):
#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')




#--------------------------------------------------------------------------- 2 - DARS  ---------------------------------------------------------------------------

########################################### 2 darsda TAble yasab oldik
# try:

#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')
       
#     #Shu yerda biz table yaratib oldik

#     sql="""CREATE TABLE insonyat (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ism TEXT NOT NULL,
#         familya TEXT NOT NULL,
#         telephone INTEGER NOT NULL,
#         email TEXT NOT NULL,
#         adress TEXT NOT NULL);"""

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)

#     conn.commit()
#     print('Table yasaldi')

#     result=cursor.fetchall()
#     print('versiyasi',result)

#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):
#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')


#-------------------------------------------------------------- 3 - DARS  ---------------------------------------------------------------------------

############################################### 3 darsda bizbazaga malumot joyladik #########################33
# try:

#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #Bu yerda biz tablega malimot qushmoqchibiza
#     sql="""INSERT INTO insonyat (ism, familya, telephone,email, adress) VALUES ('DAVRON','Boltayev',73757375,'xackercoder@gmail.com','Kattakurgan');"""

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)

#     conn.commit()
#     print('Table yasaldi')

#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):
#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')


#--------------------------------------------------------------------------- 4-DARS -------------------------------------------------------------------------

#Bu darsda biz kuplab insert yani tablga malumot qushsushni urgandik

# source_list=[('Davron','Boltayev',73757375,'Xackercoder@gmail.com','Kattakurgan'),('Davlat','boltayev',12341234,'davlatjon.com','Zavakzal')]
# try:

#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #Bu yerda biz tablega malimot qushmoqchibiza
#     sql="""INSERT INTO insonyat (ism, familya, telephone,email, adress) VALUES (?,?,?,?,?);"""

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#     #buyruqni execute ichida yozamiz
#     #execute faqat 1ta column uchun hisoblanadi
#     #cursor.execute(sql)

#     #executemany kup rowlar uchun
#     cursor.executemany(sql,source_list)

#     conn.commit()
#     print('Kup qushish bajarildi')

#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):
#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')

#----------------------------------------------------------------------- 5-Dars -----------------------------------------------------------------------------------------

# bu darsda biza terminalga malumot bazasidagi malumotni chiqrishni urgandik cursor.fetchall yordamida

# try:
#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#     sql="SELECT * FROM insonyat"

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)

#     #cursor.fetchall bu bazadan hammasini tanlab oladi
#     rows=cursor.fetchall()
#     for x in rows:
#         print('ID: ',x[0])
#         print('ISM ',x[1])
#         print('Familyasi: ',x[2])
#         print('Telefoni: ',x[3])
#         print('Emaili: ',x[4])
#         print('Manzili: ',x[5])
#         print('-'*70)

#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):

#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')

#-------------------------------------------------------------------------- 6-Dars -------------------------------------------------------------------

#Update buyruqi bn tanishamiz bugun bu SET va WHERE bilan bajariladi va bazadagi biron malumotni uzgartirish uchun kerak buladi

# try:
#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#       Bu UPDATE bazadagi malumotni yangilash uchun kerak buladi
#     sql="UPDATE insonyat SET ism='Asliddin' WHERE id=3"

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)


#     conn.commit()
    
#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):

#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')

#----------------------------------------------------------------------  7 - DARS -----------------------------------------------------------------------------------

#Create view bilan ishlash

# try:
#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')

#     bu view yasash uchun kerak buladi
#     sql="CREATE VIEW davronjon AS SELECT * FROM insonyat WHERE ism='Davron'"

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)


#     conn.commit()
    
#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):

#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')

#----------------------------------------------------------------------- 8-Dars -------------------------------------------------------------------------------------------------------------

#TABLGA USTUN(column) QUSHISH uchun
#row yani qator qushish uchun INSERT INTO deb qiymatlarni berib ketamiz

# try:
#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')


# #ALter TAble bu tablga USTUN qushib beradigan buyruq command
#     sql="""ALTER TABLE insonyat ADD ustun TEXT DEFAULT 'Qiymatlar'"""

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)


#     conn.commit()
    
#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):

#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')

#----------------------------------------------------------------------------- 9 - DARS ----------------------------------------------------------------------------------------
#Tabldagi maliumotni uchirishni urganazmi 

# try:
#     #bazani yasab olamiz
#     conn=sqlite3.connect('Bazami_ism.db')

#     #cursor yasab olamiz
#     cursor=conn.cursor()
#     print('Baza yasaldi')


# #DELETE command dasi bu barcha malumotni uchirish uchun
# #DROP commandasidan ham foydalansa buladi
#     sql="""DELETE FROM insonyat WHERE id=1"""

#     #buyruqni execute ichida yozamiz
#     cursor.execute(sql)


#     conn.commit()
    
#     #cursorni yopishimiz kerak
#     cursor.close()

# except sqlite3.Error as e:
#     print('xatolik bor ', e)

# finally:
#     if (conn):

#         #sung conn yopamiz
#         conn.close()
#         print('Boglanish tugadi!')

#------------------------------------------------------------------------- Tugadi ----------------------------------------------------------------------------------------
