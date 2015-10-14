__author__ = 'responsible'
from flask import Flask
import json
from time import time

app = Flask(__name__)

callingMapping = {"calledUser": None, "timestamp": 0}

@app.route('/<username>/videoRandomCall/')
def videoRandomCall(username):
    if callingMapping['calledUser'] in [None, username] or int(time()) - callingMapping["timestamp"] > 10:
        callingMapping['calledUser'] = username
        callingMapping['timestamp'] = int(time())
        return json.dumps({"describe": "No user online now"}), 400
    if callingMapping['calledUser'] != username:
        ret = json.dumps({"to": callingMapping['calledUser']})
        callingMapping["calledUser"] = None
        callingMapping["timestamp"] = 0
        return ret, 200

if __name__ == '__main__':
    app.run(debug=True)
