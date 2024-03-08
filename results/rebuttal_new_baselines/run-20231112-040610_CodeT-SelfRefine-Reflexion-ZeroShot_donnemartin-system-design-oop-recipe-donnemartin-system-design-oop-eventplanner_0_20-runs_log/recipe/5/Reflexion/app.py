from flask import Flask, request, jsonify
from db import db
from models import User, Recipe

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	new_user = User(username=data['username'], email=data['email'])
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'New user created'}), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	new_recipe = Recipe(title=data['title'], instructions=data['instructions'], user_id=data['user_id'])
	db.session.add(new_recipe)
	db.session.commit()
	return jsonify({'message': 'New recipe created'}), 201
