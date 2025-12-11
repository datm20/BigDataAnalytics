import datetime
import time
import os
from pymongo import MongoClient
import json

mongo_uri = "mongodb://dbstorage:27017/"
client = MongoClient(mongo_uri)
db = client["cloneDetector"]
coll_files = db["files"]
coll_chunks = db["chunks"]
coll_candidates = db["candidates"]
coll_clones = db["clones"]
coll_statuses = db["statusUpdates"]
coll_stats = db["statistics"]

WAIT_SECONDS = int(os.environ['WAIT_SECONDS'])
DEBUG = int(os.environ['MONITOR_DEBUG'])


def monitor(count, coll_name):
    coll = db[coll_name]
    if (count != coll.count_documents({})):
        count = coll.count_documents({})
        coll_stats.insert_one({"type": coll_name, "count": count , "timestamp": datetime.datetime.now() })
        
        if (DEBUG):
            # Print last inserted object
            temp = coll_stats.find({"type": coll_name}, {"type": 1, "count": 1, "timestamp": 1 }).sort("timestamp", -1).limit(1)
            print(temp.next())
    return count


if __name__ == "__main__":
    count_files = 0
    count_chunks = 0
    count_candidates = 0
    count_clones = 0
    waiting = True
    
    while(waiting):
        if("files" in db.list_collection_names()):
            waiting = False

    while(True):
        time.sleep(WAIT_SECONDS)
        count_files = monitor(count_files, "files")
        count_chunks = monitor(count_chunks, "chunks")
        count_candidates = monitor(count_candidates, "candidates")
        count_clones = monitor(count_clones, "clones")
