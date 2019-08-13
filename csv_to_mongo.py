import csv
import pymongo

connect = pymongo.MongoClient('mongodb://localhost:27017')
db=connect['db_mongo']
col=db['collection_csv']

datacsv_read=[]
with open('filecsv.csv', 'r') as y:
    reader=csv.DictReader(y)
    for i in reader:
        datacsv_read.append(dict(i))

for item in datacsv_read:
    add=col.insert_one(item)
    # print(add.inserted_id)
