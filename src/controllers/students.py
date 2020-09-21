from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
import re
from src.database import db

@app.route("/student/create/<studentname>")
def searchStudent():
    studentNameQuery = request.args.get("name")
    if not studentNameQuery:
        # Set status code to 400 BAD REQUEST
        return {
            "status": "error",
            "message": "Empty student name, please specify one"
        }, 400

    # Search a company in mongodb database
    projection = {"name": 1, "category_code": 1,"description":1}
    searchRE = re.compile(f"{studentNameQuery}", re.IGNORECASE)
    foundStudent = db["crunchbase"].find_one(
        {"name": searchRE}, projection)

    if not foundStudent:
        # Set status code to 404 NOT FOUND
        return {
            "status": "not found",
            "message": f"No student found with name {studentNameQuery} in database"
        }, 404

    data = {
        "status": "OK",
        "searchQuery": studentNameQuery,
        "student": foundStudent
    }
    return json_response(data)