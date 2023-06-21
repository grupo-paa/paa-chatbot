from flask import Flask, Blueprint, jsonify, request 
from home.home import home
from flask_cors import CORS
from auth_middleware import token_required
from pymongo import MongoClient
import jwt
import os
import bcrypt

client = MongoClient("mongodb://admin:admin@localhost:27017/")

db = client.flask_db
users = db.users
app = Flask(__name__)
app.register_blueprint(home)

app = Flask(__name__)
CORS(app)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/message', methods=['POST'])
@token_required
def post_data(current_user):
  content = request.json
  data = { 'sender':'bot', 'content': 'teste de resposta' }
  return jsonify(data)

@app.route('/login', methods=['POST'])
def login():
  user = users.insert_one({"user":"teste"})
  content = request.json
  if not content:
    return {
      "message": "Please provide user details",
      "data": None,
      "error": "Bad request"
    }, 400
  is_validated = content.get("user") == "admin" and content.get("password") == "2134"
  if not is_validated:
    return dict(message='Invalid data', data=None, error=is_validated), 400
  user = {}
  try:
    user["token"] = jwt.encode(
      {"user_id": 1},
      app.config["SECRET_KEY"],
      algorithm="HS256"
    )
    return {
      "message": "Successfully fetched auth token",
      "data": user
    }
  except Exception as e:
    return {
      "error": "Something went wrong",
      "message": str(e)
    }, 500

@app.route('/register', methods=['POST'])
def register():
  content = request.json
  if not content:
    return {
      "message": "Please provide user details",
      "data": None,
      "error": "Bad request"
    }, 400
  password = content['password'].encode('utf-8')
  hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
  print(hashed)
  try:
    users.insert_one({'user': content['user'], 'password': '2134'})
    return {
      "message": "User registered",
      "data": None,
    },200
  except Exception as e:
    return {
      "message": "Something went wrong",
      "data": None,
      "error": str(e)
    }, 500

if __name__ == "__main__":
  app.run(debug = True)
