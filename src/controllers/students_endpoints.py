from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
from src.database import db
from bson.json_util import dumps

@app.route("/student/create/", defaults = {"studentname": None})
@app.route("/student/create/<studentname>")
def createStudent(studentname):

    # Set status code to 400 BAD REQUEST
    if studentname == None:
        return {
            "status": "Error HTTP 400 (Bad Request)",
            "message": "Empty student name, please specify one"
        }

    
    """Al introducir el endpoint arriba indicado, la función se encarga de crear un nuevo estudiante dentro de la db."""

    data = {"student_name": studentname}
    newStudent = db.students.insert_one(data)
    return {"status": "ok",
        "data": f"User {studentname} has been created into students data base"
    }



@app.route("/student/all")

def searchStudent():

    """Al introducir el endpoint arriba indicado, la función se encarga de devolver una lista con los alumnos de la db."""
    
    query = db.students.distinct("student_user", {"$and": [{"student_user": {"$exists": True}},{"student_user": {"$ne": None}}]})
    return dumps(list(query))