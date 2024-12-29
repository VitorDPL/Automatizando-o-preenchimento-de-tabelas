from projeto import app, db
from flask import request, jsonify
from projeto.models import *

@app.route('/', methods=['GET'])
def home():
    return "API is running"
