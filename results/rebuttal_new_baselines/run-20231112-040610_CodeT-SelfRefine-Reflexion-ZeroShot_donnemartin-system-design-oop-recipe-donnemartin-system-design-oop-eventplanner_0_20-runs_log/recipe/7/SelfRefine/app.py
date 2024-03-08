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
	user_id = db.Column(db.String, db.ForeignKey('user.id'))
	user = db.relationship('User', backref=db.backref('recipes', lazy=True))


@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.id), 201


@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe.id), 201


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
	user = User.query.get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(user.id), 200


@app.route('/recipe/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
	recipe = Recipe.query.get(recipe_id)
	if not recipe:
		return jsonify({'error': 'Recipe not found'}), 404
	return jsonify(recipe.id), 200


if __name__ == '__main__':
	app.run(debug=True)
