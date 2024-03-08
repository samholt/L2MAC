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
	email = db.Column(db.String(120), unique=True)
	recipes = db.relationship('Recipe', backref='user', lazy=True)
	favorites = db.relationship('Favorite', backref='user', lazy=True)

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	ingredients = db.Column(db.String(500))
	instructions = db.Column(db.String(500))
	images = db.Column(db.String(500))
	categories = db.Column(db.String(500))

class Favorite(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'])
	db.session.add(user)
	db.session.commit()
	return jsonify(user), 201

@app.route('/recipe', methods=['POST'])
def create_recipe():
	data = request.get_json()
	recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], images=data['images'], categories=data['categories'], user_id=data['user_id'])
	db.session.add(recipe)
	db.session.commit()
	return jsonify(recipe), 201

if __name__ == '__main__':
	app.run(debug=True)
