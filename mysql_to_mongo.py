import mysql.connector
import pymongo

dbku=mysql.connector.connect(
    host= 'localhost',                           #127001
    user= 'root',
    password= 'nugroho21',
    # database='doraemon1'
)
connect = pymongo.MongoClient('mongodb://localhost:27017')
db=connect['db_mongo_4']
col=db['collection_mongo']

kursor=dbku.cursor()
data_input=[]
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
    data_input.append(data)  
print(data_input)
for item in data_input:
    add=col.insert_one(item)
