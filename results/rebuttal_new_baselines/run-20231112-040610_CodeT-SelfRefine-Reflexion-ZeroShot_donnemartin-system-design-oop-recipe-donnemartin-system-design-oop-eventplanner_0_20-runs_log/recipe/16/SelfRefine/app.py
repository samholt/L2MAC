from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)


class Recipe(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)


class Ingredient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	recipe_id = db.Column(db.String, db.ForeignKey('recipe.id'))


class Instruction(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String)
	recipe_id = db.Column(db.String, db.ForeignKey('recipe.id'))


class Image(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String)
	recipe_id = db.Column(db.String, db.ForeignKey('recipe.id'))


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	recipe_id = db.Column(db.String, db.ForeignKey('recipe.id'))


class Review(db.Model):
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(db.String)
	recipe_id = db.Column(db.String)
	rating = db.Column(db.Integer)
	comment = db.Column(db.String)


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
	recipe = Recipe(id=data['id'], name=data['name'])
	db.session.add(recipe)
	for ingredient in data['ingredients']:
		new_ingredient = Ingredient(name=ingredient, recipe_id=recipe.id)
		db.session.add(new_ingredient)
	for instruction in data['instructions']:
		new_instruction = Instruction(text=instruction, recipe_id=recipe.id)
		db.session.add(new_instruction)
	for image in data['images']:
		new_image = Image(url=image, recipe_id=recipe.id)
		db.session.add(new_image)
	for category in data['categories']:
		new_category = Category(name=category, recipe_id=recipe.id)
		db.session.add(new_category)
	db.session.commit()
	return jsonify(recipe), 201

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	db.session.add(review)
	db.session.commit()
	return jsonify(review), 201

if __name__ == '__main__':
	app.run(debug=True)
