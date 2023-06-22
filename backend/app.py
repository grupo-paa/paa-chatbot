from flask import Flask, Blueprint, jsonify, request 
from flask_cors import CORS
from pymongo import MongoClient
import os
client = MongoClient("mongodb+srv://admin:admin@paa-chatbot.tp4urq2.mongodb.net/?retryWrites=true&w=majority")

db = client.flask_db

app = Flask(__name__)

from auth.auth import auth
from auth_middleware import token_required
from bson.objectid import ObjectId
from messages.messages import messages

app.register_blueprint(auth)
app.register_blueprint(messages)

CORS(app)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == "__main__":
  app.run(debug = True)
