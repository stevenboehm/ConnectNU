from flask import Blueprint, request, jsonify, make_response
import json
from src import db


staff = Blueprint('staff', __name__)

@exec.route("/")
def hello_world():
    return f'<h1>Welcome to ConnectNU! You are a Staff Member!</h1>'

# Get all customers from the DB
@staff.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select committeeName from committees')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

