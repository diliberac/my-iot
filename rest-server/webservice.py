from flask import Flask, render_template, jsonify
from flask_cors import CORS
import redis
import settings as sets
import database
import os

import simulator

app = Flask(__name__)
sim = simulator.Simulator()

CORS(app)

connection = redis.Redis(host=sets.REDIS_SERVER, 
    port=sets.REDIS_PORT,
    decode_responses=True, 
    db=sets.REDIS_DB_DEFAULT)

connection.ping()

@app.route('/realtime')
def get_temperature():
    return jsonify({'temperature': connection.get('temperature')})

@app.route('/history')
def get_history():
    table = database.get_table('temperature', limit=50)
    data = [line for line in table]
    return jsonify(data)

@app.route('/simulator')
def get_simulator():
    return jsonify({'counter': sim.counter, 'random':sim.random, 'blink': sim.blink})

@app.route('/')
def default():
    if "REST_VERSION" in os.environ:
        rest_version = os.environ['REST_VERSION']
    else:
        rest_version = 'DEV'
    return render_template('index.html', rest_version=rest_version)

def main():
    app.run(host='0.0.0.0', debug=False, port='8000')

if __name__ == '__main__':
    main()
    