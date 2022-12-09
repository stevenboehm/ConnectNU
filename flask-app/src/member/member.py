from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db
from src.views import session


member = Blueprint('member', __name__)

@member.route('/memberHome/<number>', methods=['GET'])
def info(number):
    cursor = db.get_db().cursor()
    sql = "SELECT firstName from ClubMember WHERE idNumber = %s"
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@member.route('/memberHome/<number>/internalpoints', methods=["GET"])
def internalpoints(number):
    cursor = db.get_db().cursor()
    sql = "SELECT IF(COUNT(eventDate)>5, 100, (COUNT(eventDate) * 20)) as total FROM eventPoints NATURAL JOIN Events WHERE memID = %s and eventType = 'internal' GROUP BY memID"
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@member.route('/memberHome/<number>/meetingpoints', methods=["GET"])
def meetingpoints(number):
    cursor = db.get_db().cursor()
    sql = "SELECT IF(COUNT(eventDate)>5, 100, (COUNT(eventDate) * 20)) as total FROM eventPoints NATURAL JOIN Events WHERE memID = %s and eventType = 'meeting' GROUP BY memID"
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@member.route('/<number>/eventpoints', methods=["GET"])
def eventpoints(number):
    cursor = db.get_db().cursor()
    sql = "SELECT IF(COUNT(eventDate)>5, 100, (COUNT(eventDate) * 20)) as total FROM eventPoints NATURAL JOIN Events WHERE memID = %s and eventType = 'external' GROUP BY memID"
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@member.route('/memberHome/<number>/events', methods=["GET"])
def memberevents(number):
    cursor = db.get_db().cursor()
    sql = 'SELECT eventType as Category, eventDate as Date, eventTitle as Title FROM Events NATURAL JOIN eventPoints WHERE memID = %s'
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@member.route('/memberHome/<number>/dues', methods = ["GET"])
def memberdues(number):
    cursor = db.get_db().cursor()
    sql = 'SELECT dueAmount as Amount, dueTypeName as Name, paymentDate as Date FROM duePayment NATURAL JOIN dues WHERE memberID = %s'
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@member.route('/memberHome/<number>/unpaiddues', methods = ["GET"])
def unpaidDues(number):
    cursor = db.get_db().cursor()
    sql = 'SELECT dueAmount as Amount, dueTypeName as Name FROM dues LEFT JOIN (SELECT dueID, memberID from duePayment WHERE memberID = %s) as memberPay ON dues.dueID = memberPay.dueID WHERE memberID IS NULL'
    val = number
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@member.route('/memberHome/<number>/<event>', methods = ["POST"])
def checkIn(number, event):
    conn = db.connect()
    cursor = db.get_db().cursor()
    sql = "INSERT INTO eventPoints (memID, eventID) VALUES (%s, %s)"
    val = (number, event)
    cursor.execute(sql, val)
    
    conn.commit()
    return 'Done'


