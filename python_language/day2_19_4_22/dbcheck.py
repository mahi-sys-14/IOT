import pymongo
import json

f=open("config_sub.json")
config=json.loads(f.read())
f.close()

#initialise mongo db
dbclient = pymongo.MongoClient(config["db_host"],config["db_port"])
db=dbclient[config["db_name"]]
dbt=db[config["db_collection"]]

#query documents
entries = dbt.find({"topic":"devices/temp","timestamp":{"$gte":"2022-04-18T17:25:46Z","$lt":"2022-04-18T18:50:06Z"}})

#Print the entries
for entry in entries:
	print(entry)
