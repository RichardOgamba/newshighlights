from flask import Flask
from .config import DevConfig

#initialising application
app = Flask(__name__, instance_relative_config = True)

#setting up configaration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
