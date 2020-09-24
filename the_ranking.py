import os 
from dotenv import load_dotenv
load_dotenv()
import json
import requests
import re
import pandas as pd



# Creamos una función para coger las notas de cada estudiante mediante regex.
def grade(issues):
    try:
        z= re.findall(r"grade:\d+",issues[0]["body"])
        z = str(z).split(":")
        z = z[1].split("']")
        return int(z[0])
    except:
        return None



# Creamos una función para coger los memes de cada pull request mediante regex.
def meme(issues):
    try:
        meme = re.findall(r"http:.*jpg|.*jpeg|.*png",issues[0]["body"])
        meme = str(meme).split("(")
        meme = meme[1].split("'")
        return meme[0]
    except:
        return None 



def get_students(page, apiKey=os.getenv("API_GITHUB")): 
    
    """
    Get data from github using query parameters and passing a custom apikey header
    """
    
    # Compose the pulls url
    baseUrl = "https://api.github.com"
    endpoint = f"/repos/ironhack-datalabs/datamad0820/pulls/{page}"
    query_params = "?per_page=100&state=all"
    url = f"{baseUrl}{endpoint}{query_params}"
    
    
    # Compose the issues endpoint url
    baseUrl = "https://api.github.com"
    endpoint = f"/repos/ironhack-datalabs/datamad0820/issues/{page}/comments"
    query_params = "?per_page=100&state=all"
    url1 = f"{baseUrl}{endpoint}{query_params}"
    

    # Create the headers
    headers = {
        "Authorization": f"Bearer {apiKey}"
    }
    
    
    # make the request and get the response using HTTP GET verb 
    pull = requests.get(url, headers=headers)
    issue = requests.get(url1, headers=headers)
    pulls = pull.json()
    issues = issue.json()
    
    print(f"Request data to {pull.url} status_code:{pull.status_code}")
    print(f"Request data to {issue.url} status_code:{issue.status_code}")
    
    print(page)
        
    try:
        name = pulls["title"].split()[1:]
        return {"student_user": pulls["user"]["login"],
                "student_name":  " ".join(name),
                "student_id": pulls["user"]["id"],
                "pull_name": pulls["title"].split()[0].split("[")[1].split("]")[0],
                "pull_state": pulls["state"],
                "pull_created": pulls["created_at"],
                "pull_closed": pulls["closed_at"],
                "lab_number": pulls["number"],
                "grade": grade(issues),
                "meme": meme(issues)}
    except:
        return {"student_user": None,
                "student_name": None,
                "student_id": None,
                "pull_name": None,
                "pull_state": None,
                "pull_created": None,
                "pull_closed": None,
                "lab_number": None,
                "grade": None,
                "meme": None}


get_students(79)

students = [get_students(i) for i in range(1,542)]
studentsDF = pd.DataFrame(students)
studentsDF.to_json("outputs/students.json", orient="records")

# Por último importamos la base de datos a MongoDB:
# mongoimport -d the_ranking -c students --jsonArray outputs/students.json