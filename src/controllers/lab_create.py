from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
import re
from src.database import db
from bson.json_util import dumps


@app.route("/lab/create/<labname>")
def createlab(labname):

    """Al introducir el endpoint arriba indicado, la función se encarga de crear un nuevo lab dentro de la db"""
   
    data = {"pull_name": labname}

    newlab = db.students.insert_one(data)
  
    return f"New {labname} created"



"""def closed_lab(lab_name):

    projections = {"pull_name": 1, "pull_state": 1}
    query = db.students.find(({"$and": [{"pull_state": "closed"},{"pull_name": lab_name}]}), projections).count()
    return dumps(query)

def open_lab(labname):
    
    projections = {"pull_name": 1, "pull_state": 1}
    query = db.students.find(({"$and": [{"pull_state": "open"},{"pull_name": lab_name}]}), projections).count()
    return dumps(query)

def per_closed_labs(labname):
    
    projections = {"pull_name": 1, "pull_state": 1}
    query = db.students.find(({"$divide": [{"pull_state": "open"}/"pull_state": "open"}]}), projections).count()
    return dumps(query)
    
    
    """



@app.route("/lab/<lab_name>/search")
def lab_analysis(lab_name):

    """Al introducir el endpoint arriba indicado, la función se encarga de crear un nuevo lab dentro de la db"""
   
    projections = {"pull_name": 1, "pull_state": 1}
    opens = db.students.find(({"$and": [{"pull_state": "open"},{"pull_name": lab_name}]}), projections).count()
    closed = db.students.find(({"$and": [{"pull_state": "closed"},{"pull_name": lab_name}]}), projections).count()
    a = opens/closed

    dict = {"opens": opens,
    "closed": closed,
    "perc": a}
    return dict