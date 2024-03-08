from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	recipes = db.Column(db.PickleType)
	favorites = db.Column(db.PickleType)


class Recipe(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	ingredients = db.Column(db.PickleType)
	instructions = db.Column(db.PickleType)
	images = db.Column(db.PickleType)
	categories = db.Column(db.PickleType)


@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	if User.query.get(data['id']):
		return jsonify({'error': 'User already exists'}), 400
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.id), 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	user = User.query.get(id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(user.id), 200

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	user = User.query.get(id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	data = request.get_json()
	for key, value in data.items():
		setattr(user, key, value)
	db.session.commit()
	return jsonify(user.id), 200

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	user = User.query.get(id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	db.session.delete(user)
	db.session.commit()
	return jsonify({'success': 'User deleted'}), 200

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	if Recipe.query.get(data['id']):
		return jsonify({'error': 'Recipe already exists'}), 400
	recipe = Recipe(**data)
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe.id), 201

@app.route('/recipe/<id>', methods=['GET'])
def get_recipe(id):
	recipe = Recipe.query.get(id)
	if recipe is None:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify(recipe.id), 200

@app.route('/recipe/<id>', methods=['PUT'])
def update_recipe(id):
	recipe = Recipe.query.get(id)
	if recipe is None:
		return jsonify({'error': 'Recipe not found'}), 404
	data = request.get_json()
	for key, value in data.items():
		setattr(recipe, key, value)
	db.session.commit()
	return jsonify(recipe.id), 200

@app.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
	recipe = Recipe.query.get(id)
	if recipe is None:
		return jsonify({'error': 'Recipe not found'}), 404
	db.session.delete(recipe)
	db.session.commit()
	return jsonify({'success': 'Recipe deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
