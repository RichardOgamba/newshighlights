from flask import Flask
from .config import DevConfig

#initialising application
app = Flask(__name__)

#setting up configaration
app.config.from_object(DevConfig)

from app import views
