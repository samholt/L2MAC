from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
	pass

@app.route('/login', methods=['POST'])
def login():
	pass

@app.route('/profile', methods=['GET', 'PUT'])
@jwt_required
def profile():
	pass

@app.route('/post', methods=['POST', 'DELETE'])
@jwt_required
def post():
	pass

@app.route('/interact', methods=['POST'])
@jwt_required
def interact():
	pass

@app.route('/search', methods=['GET'])
@jwt_required
def search():
	pass

@app.route('/follow', methods=['POST', 'DELETE'])
@jwt_required
def follow():
	pass

@app.route('/message', methods=['POST', 'GET'])
@jwt_required
def message():
	pass

@app.route('/notification', methods=['GET'])
@jwt_required
def notification():
	pass

@app.route('/trending', methods=['GET'])
@jwt_required
def trending():
	pass

@app.route('/recommendation', methods=['GET'])
@jwt_required
def recommendation():
	pass

if __name__ == '__main__':
	app.run(debug=True)
