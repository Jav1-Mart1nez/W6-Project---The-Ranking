from src.app import app
import src.controllers.welcome
import src.controllers.students_endpoints
import src.controllers.labs_endpoints
from config import PORT

app.run("0.0.0.0", PORT, debug=True)