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
    response = requests.get('http://bodywork-rollback-deployment-test-project--stage-2:5000/v2/predict')
    if response.ok:
        app.run(host='0.0.0.0', port=5000)
    else:
        sys.exit(1)
