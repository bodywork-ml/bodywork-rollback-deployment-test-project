"""
This module defines what will happen in stage-3.
"""
import sys
import time

import requests
from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/v2/predict', methods=['GET', 'POST'])
def predict():
    return make_response(jsonify({'y': 'hello_world'}))


if __name__ == '__main__':
    time.sleep(60)
    app.run(host='0.0.0.0', port=5000)
