import mysql.connector
import csv

##deklarasi database uname dan password nya
dbku=mysql.connector.connect(
    host= 'localhost',                           #127001
    # port= 3306,
    user= 'root',
    password= 'nugroho21',
    # database='doraemon1'
)

kursor=dbku.cursor()
datacsv=[]
kolom=[]
query_db='''use doraemon1'''
kursor.execute(query_db)
querydb_idx='''describe karakter'''
kursor.execute(querydb_idx)
key=kursor.fetchall()

for i in range(0,len(key)):
    kolom.append(key[i][0])
# print(kolom)
querydb_val='''select * from karakter'''
kursor.execute(querydb_val)
val=kursor.fetchall()  

for i in range(0,len(val)):
    data={}
    for j in range(0,len(kolom)):
        data.update({kolom[j]:val[i][j]})
    datacsv.append(data) 
# print(datacsv)   

with open('mysql_to_csv.csv','w', newline='') as y:
    tulis=csv.DictWriter(y,fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(datacsv)