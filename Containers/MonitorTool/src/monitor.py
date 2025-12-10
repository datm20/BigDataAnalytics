import time
from pymongo import MongoClient
import json

mongo_uri = "mongodb://dbstorage:27017/"
client = MongoClient(mongo_uri)
db = client["cloneDetector"]
coll = db["statistics"]
mongoStat = db["statusUpdates"]

if __name__ == "__main__":
    #while(True):
        #time.sleep(2)
        #print("This is monitor talking")
        #for item in mongoStat.find():
        #    print(item)