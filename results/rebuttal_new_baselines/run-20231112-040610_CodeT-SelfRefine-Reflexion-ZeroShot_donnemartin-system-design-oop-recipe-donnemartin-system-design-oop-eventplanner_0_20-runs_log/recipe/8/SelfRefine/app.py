from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@dataclass
class User(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	name: str = db.Column(db.String)
	recipes: List[str] = db.Column(db.PickleType)
	favorites: List[str] = db.Column(db.PickleType)
	followers: List[str] = db.Column(db.PickleType)

@dataclass
class Recipe(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	name: str = db.Column(db.String)
	ingredients: List[str] = db.Column(db.PickleType)
	instructions: List[str] = db.Column(db.PickleType)
	images: List[str] = db.Column(db.PickleType)
	categories: List[str] = db.Column(db.PickleType)
	user_id: str = db.Column(db.String)

@dataclass
class Review(db.Model):
	id: str = db.Column(db.String, primary_key=True)
	user_id: str = db.Column(db.String)
	recipe_id: str = db.Column(db.String)
	rating: int = db.Column(db.Integer)
	comment: str = db.Column(db.String)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user), 201

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	data = request.get_json()
	user = User.query.get(id)
	for key, value in data.items():
		setattr(user, key, value)
	db.session.commit()
	return jsonify(user), 200

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	User.query.filter_by(id=id).delete()
	db.session.commit()
	return '', 204

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe), 201

@app.route('/recipe/<id>', methods=['PUT'])
def update_recipe(id):
	data = request.get_json()
	recipe = Recipe.query.get(id)
	for key, value in data.items():
		setattr(recipe, key, value)
	db.session.commit()
	return jsonify(recipe), 200

@app.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
	Recipe.query.filter_by(id=id).delete()
	db.session.commit()
	return '', 204

@app.route('/review', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	db.session.add(review)
	db.session.commit()
	return jsonify(review), 201

@app.route('/review/<id>', methods=['PUT'])
def update_review(id):
	data = request.get_json()
	review = Review.query.get(id)
	for key, value in data.items():
		setattr(review, key, value)
	db.session.commit()
	return jsonify(review), 200

@app.route('/review/<id>', methods=['DELETE'])
def delete_review(id):
	Review.query.filter_by(id=id).delete()
	db.session.commit()
	return '', 204

if __name__ == '__main__':
	app.run(debug=True)
