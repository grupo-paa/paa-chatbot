from flask import Blueprint, request
import jwt
import bcrypt
import os
from app import db
from app import app
from flask import current_app
from bson.objectid import ObjectId


auth = Blueprint('auth', __name__, url_prefix="/auth")

users = db.users

@auth.route('/validate', methods=['GET'])
def validate():
    users = db.users
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
    if not token:
        return {
            "message": "Authentication Token is missing!",
            "data": None,
            "error": "Unauthorized"
        }, 401
    try:
        data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        current_user = users.find_one({"_id": ObjectId(data["user_id"])})
        
        if current_user is None:
            return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        else:
            return {
               "message": "Valid Token"
            }, 200
    except Exception as e:
        return {
            "message": "Invalid Authentication token!",
            "data": None,
            "error": "Unauthorized"
        }, 500
    

@auth.route('/login', methods=['POST'])
def login():
  content = request.json
  if not content:
    return {
      "message": "Please provide user details",
      "data": None,
      "error": "Bad request"
    }, 400
  password = content['password'].encode('utf-8')
  user = users.find_one({"user":content['user']})
  print(user)
  hashed = bcrypt.hashpw(password, user['salt'])
  if(not user['password'] == hashed):
    return {"message": "Username or password invalid"},403
  try:
    user["token"] = jwt.encode(
      {"user_id": str(user["_id"])},
      app.config["SECRET_KEY"],
      algorithm="HS256"
    )
    print(user['token'])
    print(user['nickname'])
    return {
      "message": "Successfully fetched auth token",
      "data": {"token": user["token"], "nickname": user["nickname"]}
    }
  except Exception as e:
    return {
      "error": "Something went wrong",
      "message": str(e)
    }, 500

@auth.route('/register', methods=['POST'])
def register():
  content = request.json
  if not content:
    return {
      "message": "Please provide user details",
      "data": None,
      "error": "Bad request"
    }, 400
  password = content['password'].encode('utf-8')
  salt = bcrypt.gensalt(10)
  hashed = bcrypt.hashpw(password, salt)
  try:
    users.insert_one({'user': content['user'], 'password': hashed, 'salt': salt, 'messages': [], 'nickname': content['nickname']})
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

