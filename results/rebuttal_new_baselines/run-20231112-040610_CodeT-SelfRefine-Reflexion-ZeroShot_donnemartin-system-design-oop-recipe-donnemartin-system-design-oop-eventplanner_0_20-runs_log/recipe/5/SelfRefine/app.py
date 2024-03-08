from flask import Flask, request, jsonify
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Database models

favorites = db.Table('favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'))
)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	recipes = db.relationship('Recipe', backref='user', lazy=True)
	favorites = db.relationship('Recipe', secondary=favorites, lazy='subquery', backref=db.backref('users', lazy=True))

	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	ingredients = db.Column(db.String(200))
	instructions = db.Column(db.String(200))
	images = db.Column(db.String(200))
	categories = db.Column(db.String(50))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

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

@app.route('/recipe', methods=['GET'])
def get_recipes():
	recipes = Recipe.query.all()
	return jsonify([recipe.to_dict() for recipe in recipes]), 200

@app.route('/recipe/<name>', methods=['GET'])
def get_recipe(name):
	recipe = Recipe.query.filter_by(name=name).first()
	if recipe:
		return jsonify(recipe.to_dict()), 200
	else:
		return {'message': 'Recipe not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
