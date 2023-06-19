from flask import Flask, Blueprint, jsonify, request 
from home.home import home
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(home)

app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['POST'])
def post_data():
  content = request.json
  print(content['message'])
  data = { 'response': 'teste de resposta' }
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug = True)
