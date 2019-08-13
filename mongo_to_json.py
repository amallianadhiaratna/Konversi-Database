import json
import pymongo

connect = pymongo.MongoClient('mongodb://localhost:27017')
db=connect['db_mongo']
col=db['collection_csv']

list_1=list(col.find())

for j in range(0,len(list_1)):
    list_1[j].pop('_id')

with open('writejson_from_mongo.json','w') as x:
    json.dump(list_1,x)