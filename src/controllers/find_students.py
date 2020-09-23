from src.app import app
from flask import request, Response
from src.database import db
from bson.json_util import dumps

@app.route("/student/all")

def searchStudent():

    """Al introducir el endpoint arriba indicadp, la función se encarga de devolver una lista con los alumnos de la db"""

    query = db.students.find({"$and": [{"student_user": {"$exists": True}},{"student_user": {"$ne": "null"}}]})
    return dumps(list(query))

