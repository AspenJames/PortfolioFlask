from flask import Flask

# Initialize app object
# instance_relative_config allows app.config.from_object('config')
# to load the config.py file
app = Flask(__name__, instance_relative_config=True)

# Load views
from app import views

# Load config
app.config.from_object('config')
