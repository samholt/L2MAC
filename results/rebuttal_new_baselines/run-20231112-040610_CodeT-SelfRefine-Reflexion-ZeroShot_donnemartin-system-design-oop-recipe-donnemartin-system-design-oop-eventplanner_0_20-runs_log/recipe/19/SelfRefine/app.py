from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models
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

@app.route('/recipe/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
	data = request.get_json()
	recipe = Recipe.query.get(recipe_id)
	if not recipe:
		return {'message': 'Recipe not found'}, 404
	recipe.name = data.get('name', recipe.name)
	recipe.ingredients = data.get('ingredients', recipe.ingredients)
	recipe.instructions = data.get('instructions', recipe.instructions)
	recipe.images = data.get('images', recipe.images)
	recipe.categories = data.get('categories', recipe.categories)
	db.session.commit()
	return jsonify(recipe), 200

@app.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
	recipe = Recipe.query.get(recipe_id)
	if not recipe:
		return {'message': 'Recipe not found'}, 404
	db.session.delete(recipe)
	db.session.commit()
	return {'message': 'Recipe deleted'}, 200

@app.route('/recipe/search', methods=['GET'])
def search_recipe():
	query = request.args.get('query')
	results = Recipe.query.filter(Recipe.name.contains(query) | Recipe.ingredients.contains(query) | Recipe.categories.contains(query) | Recipe.instructions.contains(query) | Recipe.reviews.contains(query)).all()
	return jsonify(results), 200

if __name__ == '__main__':
	app.run(debug=True)
