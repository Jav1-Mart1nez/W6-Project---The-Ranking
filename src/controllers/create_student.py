from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
import re
from src.database import db


@app.route("/student/create/<studentname>")
def createStudent(studentname):
   
    data = {"student_name": studentname}

    newStudent = db.students.insert_one(data)
  
    return f"User {studentname} created"

    """return json_response(data)"""