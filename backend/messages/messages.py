from flask import Blueprint, jsonify, request
import jwt
import bcrypt
import os
from app import db
from app import app
from auth_middleware import token_required

messages = Blueprint('messages', __name__, url_prefix="/messages")

users = db.users
ITEMS_PER_PAGE = 5

@messages.route('/send_message', methods=['POST'])
@token_required
def post_data(current_user):
  content = request.json
  messages = current_user['messages']

  data = { 'sender':'bot', 'content': 'teste de resposta' }
  messages.append({'sender': str(current_user['_id']), 'content': content['message']})
  messages.append(data)
  update = {"$set":{"messages": messages}}
  filterDb = {"_id": current_user["_id"]}
  users.update_one(filterDb, update)

  return jsonify(data)


@messages.route('/get_messages', methods=['POST'])  # Identificar a pagina via query string Ex. ...?page=2
@token_required
def get_messages(current_user):
  messages = current_user['messages']
  page = int(request.args.get('page')) or 1
  first_index = ITEMS_PER_PAGE*(page-1)
  last_slice_index = (ITEMS_PER_PAGE*page)

  return jsonify({
    "messages": messages[first_index:last_slice_index]
  })
