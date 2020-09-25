from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response

@app.route("/")

def welcome():
    return {
        "1) message": "Welcome to the ranking api",
        "2) status": "OK",
        "3) instructions": "Please visit the following url 'https://github.com/Jav1-Mart1nez/W6-Project---The-Ranking/blob/master/README.md'"
    }
