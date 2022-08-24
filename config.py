
import os
from os import environ

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/techhunt'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle': 299}
