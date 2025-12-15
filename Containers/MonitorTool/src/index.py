from flask import Flask, current_app, request, render_template, Response, jsonify
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
coll_statuses = db["statusUpdates"]
coll_stat = db["statistics"]


@app.route("/")
def index():
    updates = coll_statuses.find({}, {})

    files = coll_stat.find({"type": "files"}, {"type": 1, "count": 1, "timestamp": 1 }).limit(100)
    chunks = coll_stat.find({"type": "chunks"}, {"type": 1, "count": 1, "timestamp": 1 }).limit(100)
    candidates = coll_stat.find({"type": "candidates"}, {"type": 1, "count": 1, "timestamp": 1 }).limit(100)
    clones = coll_stat.find({"type": "clones"}, {"type": 1, "count": 1, "timestamp": 1 }).limit(100)


    return render_template('index.html', updates = updates, files = files, chunks = chunks, candidates = candidates, clones = clones)


@app.route("/chunks")
def chunks():    
    array = coll_stat.find({"type": "chunks"}, {"type": 1, "count": 1, "timestamp": 1 })

    if ("files" in db.list_collection_names()):
        avg_chunks_per_file = round(coll_chunks.count_documents({}) / coll_files.count_documents({}), 2)
    
    #amount of processed and processed/time
    first_time = True
    last_count = 0
    last_time = 0
    averages = []
    for item in array: 
        if (first_time):
            last_count = item["count"]
            last_time = item["timestamp"]
            first_time = False
            continue

        chunks_per_sec = (item["count"] - last_count)/((item["timestamp"] - last_time).total_seconds())
        averages.append({"x": item["count"], "y": chunks_per_sec})
        
        last_count = item["count"]
        last_time = item["timestamp"]


    #Time and amount of processed
    time_amount = []
    start_time = 0
    array = coll_stat.find({"type": "chunks"}, {"type": 1, "count": 1, "timestamp": 1 })
    for item in array: 
        if (start_time == 0):
            start_time = item["timestamp"]
        time_amount.append({"x": (item["timestamp"] - start_time).total_seconds(), "y": item["count"]})

    return render_template('chunks.html', chunks = averages, amount = time_amount,  chunks_per_file = avg_chunks_per_file)


@app.route("/files")
def files():
    array = coll_stat.find({"type": "files"}, {"type": 1, "count": 1, "timestamp": 1 })

    first_time = True
    last_count = 0
    last_time = 0
    averages = []
    for item in array:
        if (first_time):
            last_count = item["count"]
            last_time = item["timestamp"]
            first_time = False
            continue

        files_per_sec = (item["count"] - last_count)/((item["timestamp"] - last_time).total_seconds())
        averages.append({"x": item["count"], "y": files_per_sec})
        
        last_count = item["count"]
        last_time = item["timestamp"]


    #Time and amount of processed
    time_amount = []
    start_time = 0
    array2 = coll_stat.find({"type": "files"}, {"type": 1, "count": 1, "timestamp": 1 })
    for item in array2: 
        if (start_time == 0):
            start_time = item["timestamp"]
        time_amount.append({"x": (item["timestamp"] - start_time).total_seconds(), "y": item["count"]})


    return render_template('files.html', files = averages, amount = time_amount)


@app.route("/candidates")
def candidates():
    array = coll_stat.find({"type": "candidates"}, {"type": 1, "count": 1, "timestamp": 1 })

    first_time = True
    last_count = 0
    last_time = 0
    start_time = 0
    averages = []
    for item in array:
        if (first_time):
            start_time = item["timestamp"]
            last_count = item["count"]
            last_time = item["timestamp"]
            first_time = False
            continue

       
        candidates_per_sec = (item["count"] - last_count)/((item["timestamp"] - last_time).total_seconds())
        averages.append({"x": (item["timestamp"] - start_time).total_seconds(), "y": candidates_per_sec*(-1)})
        
        last_count = item["count"]
        last_time = item["timestamp"]
    
    #Time and amount of processed
    time_amount = []
    start_time = 0
    array2 = coll_stat.find({"type": "candidates"}, {"type": 1, "count": 1, "timestamp": 1 })
    for item in array2: 
        if (start_time == 0):
            start_time = item["timestamp"]
        time_amount.append({"x": (item["timestamp"] - start_time).total_seconds(), "y": item["count"]})

    return render_template('candidates.html', candidates = averages, amount = time_amount)


@app.route("/clones")
def clones():


    clones_size = 0
    temp = coll_clones.find({}, {"instances": 1})
    for i in temp:
        clones_size += (i["instances"][0]["endLine"] - i["instances"][0]["startLine"])


    avg_clone_size = round(clones_size/coll_clones.count_documents({}), 2) 

    
    array = coll_stat.find({"type": "clones"}, {"type": 1, "count": 1, "timestamp": 1 })

    first_time = True
    last_count = 0
    last_time = 0
    averages = []
    for item in array:
        if (first_time):
            last_count = item["count"]
            last_time = item["timestamp"]
            first_time = False
            continue

        clones_per_sec = (item["count"] - last_count)/((item["timestamp"] - last_time).total_seconds())
        averages.append({"x": item["count"], "y": clones_per_sec})
        
        last_count = item["count"]
        last_time = item["timestamp"]
    

    #Time and amount of processed
    time_amount = []
    start_time = 0
    array2 = coll_stat.find({"type": "clones"}, {"type": 1, "count": 1, "timestamp": 1 })
    for item in array2: 
        if (start_time == 0):
            start_time = item["timestamp"]
        time_amount.append({"x": (item["timestamp"] - start_time).total_seconds(), "y": item["count"]})


    return render_template('clones.html', clones = averages, amount = time_amount, clone_size = avg_clone_size)
