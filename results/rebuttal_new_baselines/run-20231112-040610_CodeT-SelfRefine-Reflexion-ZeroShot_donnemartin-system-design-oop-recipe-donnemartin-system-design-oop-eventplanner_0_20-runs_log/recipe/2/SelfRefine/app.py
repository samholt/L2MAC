from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	recipes = db.relationship('Recipe', backref='user', lazy=True)
	favorites = db.relationship('Recipe', secondary='favorite', backref='favorited_by', lazy=True)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	ingredients = db.Column(db.PickleType, nullable=False)
	instructions = db.Column(db.PickleType, nullable=False)
	images = db.Column(db.PickleType, nullable=False)
	categories = db.Column(db.PickleType, nullable=False)
	reviews = db.Column(db.PickleType, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

favorite = db.Table('favorite',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if User.query.filter_by(username=username).first() is not None:
		return jsonify({'message': 'User already exists'}), 400
	user = User(username=username)
	user.set_password(password)
	db.session.add(user)
	db.session.commit()
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User.query.filter_by(username=username).first()
	if user is None or not user.check_password(password):
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
	data = request.get_json()
	username = data['username']
	user = User.query.filter_by(username=username).first()
	if user is None:
		return jsonify({'message': 'User not found'}), 400
	recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'], images=data['images'], categories=data['categories'], reviews=[], user=user)
	db.session.add(recipe)
	db.session.commit()
	return jsonify({'message': 'Recipe submitted successfully'}), 200

@app.route('/edit_recipe', methods=['POST'])
def edit_recipe():
	data = request.get_json()
	username = data['username']
	recipe_id = data['recipe_id']
	user = User.query.filter_by(username=username).first()
	if user is None:
		return jsonify({'message': 'User not found'}), 400
	recipe = Recipe.query.get(recipe_id)
	if recipe is None or recipe.user != user:
		return jsonify({'message': 'Recipe not found'}), 400
	recipe.name = data.get('name', recipe.name)
	recipe.ingredients = data.get('ingredients', recipe.ingredients)
	recipe.instructions = data.get('instructions', recipe.instructions)
	recipe.images = data.get('images', recipe.images)
	recipe.categories = data.get('categories', recipe.categories)
	db.session.commit()
	return jsonify({'message': 'Recipe edited successfully'}), 200

@app.route('/delete_recipe', methods=['POST'])
def delete_recipe():
	data = request.get_json()
	username = data['username']
	recipe_id = data['recipe_id']
	user = User.query.filter_by(username=username).first()
	if user is None:
		return jsonify({'message': 'User not found'}), 400
	recipe = Recipe.query.get(recipe_id)
	if recipe is None or recipe.user != user:
		return jsonify({'message': 'Recipe not found'}), 400
	db.session.delete(recipe)
	db.session.commit()
	return jsonify({'message': 'Recipe deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
