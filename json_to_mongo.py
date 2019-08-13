import json
import pymongo

connect = pymongo.MongoClient('mongodb://localhost:27017')
db=connect['db_mongo_2']

col=db['collection_json']
datajson_read=[]
with open('filejson.json') as x:
    datajson_read=json.load(x)
print(datajson_read)

for item in datajson_read:
    add=col.insert_one(item)
    # print(add.inserted_id)