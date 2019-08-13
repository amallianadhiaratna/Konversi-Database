import csv
import pymongo

connect = pymongo.MongoClient('mongodb://localhost:27017')
db=connect['db_mongo']
col=db['collection_csv']

list_1=list(col.find())

for j in range(0,len(list_1)):
    list_1[j].pop('_id')

#write csv
with open('writecsv_from_mongo.csv','w', newline='') as y:
    kolom=list(list_1[0].keys())
    tulis=csv.DictWriter(y,fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(list_1)