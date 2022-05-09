from flask import Flask
import json
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    data_set = {'page': 'Home',
                'Class': 'Normal', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump
