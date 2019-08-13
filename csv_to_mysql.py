import mysql.connector
import csv

dbku=mysql.connector.connect(
    host= 'localhost',                           #127001
    user= 'root',
    password= 'nugroho21',
    # database='doraemon1'
)

kursor=dbku.cursor()
datacsv_read=[]
with open('filecsv_baru.csv', 'r') as y:
    reader=csv.DictReader(y)
    for i in reader:
        # print(dict(i))
        datacsv_read.append(dict(i))
print(datacsv_read)

kursor.execute('create database NewDatabase_1')
kursor.execute('''use newdatabase_1''')
querydb='''create table table_1(
    id int not null auto_increment,
    nama varchar(30),
    usia smallint,
    primary key (id)
)'''
kursor.execute(querydb)

datamysql=[]
for j in range(0,len(datacsv_read)):
    data=[]
    for key in datacsv_read[j].keys():
        data.append(datacsv_read[j][key])
    datamysql.append(tuple(data)) 
print(datamysql)   
querydb='''insert into karakter(id, nama, usia) values  (%s, %s, %s)'''     ##d digit s string
kursor.executemany(querydb,datamysql)
dbku.commit()