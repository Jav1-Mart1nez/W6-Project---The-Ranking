from src.app import app
import src.controllers.create_student
import src.controllers.find_students
import src.controllers.lab_create
from config import PORT

app.run("0.0.0.0", PORT, debug=True)