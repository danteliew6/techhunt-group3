from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import not_, func
from src.splitbill import db
from datetime import datetime
import json
import functools

class ApiController():
    
    def addTeams():
        data = request.get_json()