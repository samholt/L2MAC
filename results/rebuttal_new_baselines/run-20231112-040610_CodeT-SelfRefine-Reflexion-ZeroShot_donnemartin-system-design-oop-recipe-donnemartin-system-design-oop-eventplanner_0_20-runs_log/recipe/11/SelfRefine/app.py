from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import List
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	recipes = db.Column(db.PickleType)
	favorites = db.Column(db.PickleType)

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Recipe(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	ingredients = db.Column(db.PickleType)
	instructions = db.Column(db.PickleType)
	images = db.Column(db.PickleType)
	categories = db.Column(db.PickleType)
	reviews = db.Column(db.PickleType)

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Category(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	recipes = db.Column(db.PickleType)

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(**data)
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe.to_dict()), 201

@app.route('/category', methods=['POST'])
def create_category():
	data = request.get_json()
	category = Category(**data)
	db.session.add(category)
	db.session.commit()
	return jsonify(category.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
