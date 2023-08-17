import time
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/time')
def current_time():
   return {
        "time" : time.time()
   }
       
       