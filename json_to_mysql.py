import mysql.connector
import json

dbku=mysql.connector.connect(
    host= 'localhost',                           #127001
    # port= 3306,
    user= 'root',
    password= 'nugroho21',
    # database='doraemon1'
)

kursor=dbku.cursor()
# kursor.execute('create database NewDatabase_3')
kursor.execute('''use newdatabase_3''')
# querydb='''create table table_3(
#     id int not null auto_increment,
#     nama varchar(30),
#     usia smallint,
#     primary key (id)
# )'''
# kursor.execute(querydb)

with open('filejson.json') as x:
    datajson_read=json.load(x)
print(datajson_read)
datajson_new=[]
for j in range(0,len(datajson_read)):
    data=[]
    for key in datajson_read[j].keys():
        data.append(datajson_read[j][key])
    datajson_new.append(tuple(data)) 
print(datajson_new)   
querydb='''insert into table_3(id, nama, usia) values  (%s, %s, %s)'''     ##d digit s string
kursor.executemany(querydb,datajson_new)
dbku.commit()
