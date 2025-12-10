from flask import Flask, current_app, request, render_template, Response
from pymongo import MongoClient
from bson import json_util, ObjectId
from bson.errors import InvalidId
import json
import os
import datetime

template_folder_path = os.path.join('static', 'templates')

app = Flask(__name__, template_folder=template_folder_path)

mongo_uri = "mongodb://dbstorage:27017/"
client = MongoClient(mongo_uri)
db = client["cloneDetector"]
coll_files = db["files"]
coll_chunks = db["chunks"]
coll_candidates = db["candidates"]
coll_clones = db["clones"]
coll_stat = db["statusUpdates"]

@app.route("/")
def statistics():
    averages = []
    chunks = coll_chunks.find({}, {"timestamp":1}).limit(100)
    chunks2 = coll_chunks.find({}, {"timestamp":1})
    #print(chunks)
    last = 0
    for i in chunks:
        #print(datetime.datetime.strptime(i["timestamp"][:-3], "%Y-%m-%dT%H:%M:%S.%f")) #2025-12-10T13:20:37.786640186
        current = datetime.datetime.strptime(i["timestamp"][:-3], "%Y-%m-%dT%H:%M:%S.%f")
        if last != 0:
            #print(i["timestamp"])
            
            averages.append( current - last )
            
        
        
        last = current
    #print(averages)

    return render_template('index.html', chunks=chunks2)


@app.route("/chunks")
def chunks():
    


    return render_template('index.html')#, data=json_data)