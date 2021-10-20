"""
This module defines what will happen in stage-3.
"""
import sys

import requests
from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/v2/predict', methods=['GET', 'POST'])
def predict():
    return make_response(jsonify({'y': 'hello_world'}))


if __name__ == '__main__':
    try:
        response = requests.get('http://stage-2:5000/v2/predict')
    except requests.exceptions.ConnectionError:
        sys.exit(1)
    finally:
        app.run(host='0.0.0.0', port=5000)
