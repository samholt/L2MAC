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
	recipe = Recipe(**data)
	db.session.add(recipe)
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
