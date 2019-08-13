import mysql.connector
import pymongo

dbku=mysql.connector.connect(
    host= 'localhost',                           #127001
    # port= 3306,
    user= 'root',
    password= 'nugroho21',
    # database='doraemon1'
)
connect = pymongo.MongoClient('mongodb://localhost:27017')
db=connect['db_mongo']
col=db['collection_csv']
kursor=dbku.cursor()
kursor.execute('create database db_mongo_mysql')
kursor.execute('''use db_mongo_mysql''')
querydb='''create table table_mongo_mysql(
    id int not null auto_increment,
    nama varchar(30),
    usia smallint,
    primary key (id)
)'''
kursor.execute(querydb)
list_1=list(col.find())

for j in range(0,len(list_1)):
    list_1[j].pop('_id')

datamysql_new=[]
for j in range(0,len(list_1)):
    data=[]
    for key in list_1[j].keys():
        data.append(list_1[j][key])
    datamysql_new.append(tuple(data)) 
print(datamysql_new)  
querydb='''insert into table_mongo_mysql(id, nama, usia) values  (%s, %s, %s)'''     ##d digit s string
kursor.executemany(querydb,datamysql_new)
dbku.commit()