from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
recipes = {}

@dataclass
class User:
	id: str
	name: str

@dataclass
class Recipe:
	id: str
	name: str
	ingredients: list
	instructions: str
	image: str
	user_id: str

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(dataclass_to_dict(user)), 201

@app.route('/recipes', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	recipes[recipe.id] = recipe
	return jsonify(dataclass_to_dict(recipe)), 201

def dataclass_to_dict(dataclass_instance):
	return {k: v for k, v in dataclass_instance.__dict__.items()}
