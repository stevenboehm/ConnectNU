from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for, session
from src import db
views = Blueprint('views', __name__)



@views.route('/', methods = ["GET"])
def home():
    return "Welcome"

@views.route('/input', methods = ["POST", "GET"])
def input():
    conn = db.connect()
    current_app.logger.info(request.form)
    id = request.form['idNumber']
    first = request.form['firstName']
    last = request.form['lastName']
    coll = request.form['college']
    yearr = request.form['year']
    cursor=db.get_db().cursor()
    sql = "INSERT INTO ClubMember (idNumber, firstName, lastName, college, year) VALUES (%s, %s, %s, %s, %s)"
    val = (id, first, last, coll, yearr)
    cursor.execute(sql, val)
    
    conn.commit()
    return None

# This is a sample route for the /test URI.  
# as above, it just returns a simple string. 
@views.route('/test')
def tester():
    return "<h1>this is a test!</h1>"

@views.route('/test_db', methods = ["GET"])
def getCommittees():
    cursor = db.get_db().cursor()
    cursor.execute('select * from committees')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@views.route('/execs', methods = ["GET"])
def execs():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT leaderID FROM committeeLeader')
    data = []
    theData = cursor.fetchall()
    for row in theData:
        data.append(row[0])
    return data

@views.route('/supervisors', methods = ["GET"])
def supervisors():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT staffID from supervisor')
    data = []
    theData = cursor.fetchall()
    for row in theData:
        data.append(row[0])
    return data

@views.route('/members', methods = ["GET"])
def members():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT idNumber from ClubMember')
    data = []
    theData = cursor.fetchall()
    for row in theData:
        data.append(row[0])
    return data