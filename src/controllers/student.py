import numpy as np
from src.app import app
from flask import request


@app.route('/')
def welcome():
    return {
        "status": "OK",
        "message": "Welcome to ranking_API"
    }


def crateStudent(studentname):
    return student_id


@app.route("/student/create/studentname")
def student():
    return {
        "student": crateStudent()
    }
