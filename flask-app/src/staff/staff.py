from flask import Blueprint, request, jsonify, make_response, current_app
import json
import logging
from src import db



staff = Blueprint('staff', __name__)

@staff.route('/staffHome/<number>', methods=['GET'])
def info(number):
    cursor = db.get_db().cursor()
    sql = "SELECT firstName from supervisor WHERE staffID = %s"
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

@staff.route('/staffHome/payments')
def payments():
    cursor = db.get_db().cursor()
    sql = "SELECT dueAmount as Amount, paymentDate as 'Payment Date', firstName as 'First Name', lastName as 'Last Name' from duePayment JOIN ClubMember on duePayment.memberID = ClubMember.idNumber NATURAL JOIN dues"
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

@staff.route('/staffHome/dues')
def dues():
    cursor = db.get_db().cursor()
    sql = "SELECT dueID, dueTypeName from dues"
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

@staff.route('/staffHome/inputpayment', methods = ["POST", "GET"])
def input():
    conn = db.connect()
    current_app.logger.info(request.form)
    id = request.form['idNumber']
    date = request.form['PayDate']
    category = request.form['Category']
    cursor=db.get_db().cursor()
    sql = "INSERT INTO duePayment (memberID, paymentDate, dueID) VALUES (%s, %s, %s)"
    val = (id, date, category)
    cursor.execute(sql, val)
    
    conn.commit()
    return "hello"