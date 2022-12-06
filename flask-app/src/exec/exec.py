from flask import Blueprint, request, jsonify, make_response, current_app
import json
import logging
from src import db
import qrcode
import base64
import io



exec = Blueprint('exec', __name__)


@exec.route('/execHome/<number>', methods = ["GET"])
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

@exec.route('/execHome/<number>/roster', methods = ["GET"])
def roster(number):
    cursor = db.get_db().cursor()
    sql = "SELECT * from ClubMember"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@exec.route('/execHome/<number>/calendar', methods = ["GET"])
def calendar(number):
    cursor = db.get_db().cursor()
    sql = "SELECT eventDate as Date, eventType as Category, eventTitle as Title, eventID from Events"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@exec.route('/execHome/qr/<event>', methods = ["GET"])
def qr(event):
    img = qrcode.make(event)
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    jsoned = make_response(jsonify([{"string" : img_str.decode('utf-8')}]))
    return jsoned

@exec.route('/execHome/events', methods = ["GET"])
def events():
    cursor = db.get_db().cursor()
    sql = "SELECT eventType from Events"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@exec.route('/execHome/numEvent', methods = ["GET"])
def numEvent():
    cursor=db.get_db().cursor()
    sql = "SELECT MAX(eventID) as maximum from Events"
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    maximum = make_response(jsonify((json_data[0]["maximum"] + 1)))
    return maximum

@exec.route('/execHome/addEvent/<eventID>', methods = ["POST"])
def addEvent(eventID):
    conn = db.connect()
    current_app.logger.info(request.form)
    title = request.form['title']
    date = request.form['EventDate']
    category = request.form['Category']
    cursor=db.get_db().cursor()
    sql = "INSERT INTO Events (eventID, eventType, eventDate, eventTitle) VALUES (%s, %s, %s, %s)"
    val = (eventID, category, date, title)
    cursor.execute(sql, val)
    
    conn.commit()
    return 'Done'