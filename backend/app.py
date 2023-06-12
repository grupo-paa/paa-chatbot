from flask import Flask, Blueprint, jsonify  
from home.home import home
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(home)

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
  data = { 'message': 'Hello from Flask!' }
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug = True)
