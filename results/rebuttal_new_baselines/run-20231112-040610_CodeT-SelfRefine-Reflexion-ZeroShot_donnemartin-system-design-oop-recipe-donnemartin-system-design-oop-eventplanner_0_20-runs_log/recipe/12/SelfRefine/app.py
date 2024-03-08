from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	recipes = db.relationship('Recipe', backref='user', lazy=True)
	favorites = db.relationship('Favorite', backref='user', lazy=True)

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)
	instructions = db.relationship('Instruction', backref='recipe', lazy=True)
	images = db.relationship('Image', backref='recipe', lazy=True)
	categories = db.relationship('Category', backref='recipe', lazy=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Ingredient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Instruction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	step = db.Column(db.String(500))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Image(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(500))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

class Favorite(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe), 201

@app.route('/recipe/<name>', methods=['PUT'])
def update_recipe(name):
	data = request.get_json()
	recipe = Recipe.query.filter_by(name=name).first()
	if recipe:
		recipe.ingredients = data.get('ingredients', recipe.ingredients)
		recipe.instructions = data.get('instructions', recipe.instructions)
		recipe.images = data.get('images', recipe.images)
		recipe.categories = data.get('categories', recipe.categories)
		db.session.commit()
		return jsonify(recipe), 200
	else:
		return {'message': 'Recipe not found'}, 404

@app.route('/recipe/<name>', methods=['DELETE'])
def delete_recipe(name):
	recipe = Recipe.query.filter_by(name=name).first()
	if recipe:
		db.session.delete(recipe)
		db.session.commit()
		return {'message': 'Recipe deleted'}, 200
	else:
		return {'message': 'Recipe not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
