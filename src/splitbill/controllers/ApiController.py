from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from ..models.User import User
from flask_cors import CORS
from sqlalchemy import not_, func
from src.splitbill import db
from datetime import datetime
import json
import functools

class ApiController():
    
    # message -> Cost of food and id of who ate
    def two():
        data = request.get_json()
        message = data['message']
        message = message.split(',')
        cost = message[0]
        people = message[1:]
        avg_cost = cost / len(people)
        for person in people:
            
        
        # .....
        # return jsonify({
        #         "message": str(e)
                # "next": "endpoint for the next api and bid"
        #     }), 400