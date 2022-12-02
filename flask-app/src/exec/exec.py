from flask import Blueprint, request, jsonify, make_response
import json
from src import db


exec = Blueprint('exec', __name__)

@exec.route("/")
def hello_world():
    return f'<h1>Welcome to ConnectNU! You are an Executive Board Member!</h1>'

# Get all the members from the database
@exec.route('/members', methods=['GET'])
def get_products():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('select idNumber, firstName, lastName from ClubMember')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

