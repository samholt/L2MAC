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
	reviews = db.Column(db.PickleType)


@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	if not all(key in data for key in ('id', 'name', 'recipes', 'favorites')):
		return jsonify({'error': 'Missing fields in request data'}), 400
	if User.query.get(data['id']):
		return jsonify({'error': 'User already exists'}), 400
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.id), 201


@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	if not all(key in data for key in ('id', 'name', 'ingredients', 'instructions', 'images', 'categories', 'reviews')):
		return jsonify({'error': 'Missing fields in request data'}), 400
	if Recipe.query.get(data['id']):
		return jsonify({'error': 'Recipe already exists'}), 400
	recipe = Recipe(**data)
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe.id), 201


if __name__ == '__main__':
	app.run(debug=True)
