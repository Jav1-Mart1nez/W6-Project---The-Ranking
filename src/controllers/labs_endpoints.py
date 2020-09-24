from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
from src.database import db
from bson.json_util import dumps


@app.route("/lab/create/<lab_name>")
def createlab(lab_name):

    """Al introducir el endpoint arriba indicado, la función se encarga de crear un nuevo lab dentro de la students db."""
   
    # New data lab.
    data = {"pull_name": lab_name}
    newlab = db.students.insert_one(data)
  
    return f"The lab {labname} has been created into students data base"



@app.route("/lab/<lab_name>/search")
def lab_analysis(lab_name):

    """Al introducir el endpoint arriba indicado, la función devuelve un diccionario con un análisis estadístico de las pull request."""
    
    # Number of open PR.
    opened = db.students.find({"$and": [{"pull_state": "open"},{"pull_name": lab_name}]}).count()
    
    # Number of closed PR.
    closed = db.students.find({"$and": [{"pull_state": "closed"},{"pull_name": lab_name}]}).count()
    
    # Percentage of completeness (closed vs open).
    perc_completeness  = int(closed/(opened+closed)*100)

    # List number of students for each PR.
    stu_projections = {"student_user": 1}
    students = db.students.find(({"pull_name": lab_name}), stu_projections).distinct("student_user")
    students = dumps(list(students)) 
    
    # List memes for each PR.
    memes = db.students.find({"$and": [{"meme": {"$ne": None}},{"pull_name": lab_name}]}).distinct("meme")
    memes = dumps(list(memes))

    # Grade for each PR.
    gra_projections = {"student_user": 1, "grade": 1}
    grade = db.students.find(({"$and": [{"grade": {"$ne": None}},{"pull_name": lab_name}]}), gra_projections)
    grade = dumps(list(grade))

    # No conseguí sacar la diferencia de tiempos.
    """Instructor grade time in hours: (pr_close_time-last_commit_time).
    fecha = db.students.aggregate([{"$project": {"pull_name": lab_name, "dateDifference": {"$subtract": [ "$ISODate(pull_closed)", "$ISODate(pull_created)" ]}}}])
    fecha = db.students.aggregate([{"$project": {"duration": {"$divide": [{"$subtract": ["$ISODate(pull_closed)", "$ISODate(pull_created)"]}, 3600000]}}}])
    fecha = dumps(list(fecha))"""

    
    Analysis = {
                "1) Open Pull Request": opened,
                "2) Closed Pull Request": closed,
                "3) Percentage of completeness": perc_completeness,
                "4) List number of students for each PR": students,
                "5) List memes for each PR.": memes,
                "6) Grades of students for each PR": grade
                }
    
    return Analysis


# No conseguí sacar el memeranking
"""@app.route("/lab/memeranking")
def memeranging():

    memeranging = db.students.aggregate(
       {"$match": {"meme" :{ "$ne" : None } } }, 
       {"$group" : {"_id": "$meme", "count": { "$sum": 1 } } },
       {"$match": {"count" : {"$gt": 1} } }, 
       {"$project": {"meme" : "$_id", "_id" : 0} }
)
    #memeranging = db.students.aggregate({"$group": {"_id" : "$meme", "count" : {"$sum" : 1}}}).result
    return dumps(list(memeranging))"""



@app.route("/lab/<lab_name>/meme")
def random_meme(lab_name):

    """Al introducir el endpoint arriba indicado, la función devuelve un meme aleatorio del lab solicitado."""
    
    meme_projections = {"meme":1}
    random_meme = db.students.aggregate([{"$match": {"$and": [{"pull_name": lab_name}, {"meme": {"$ne": None}}]}}, {"$sample": {"size": 1}}, {"$project": meme_projections}])
    return dumps(list(random_meme))