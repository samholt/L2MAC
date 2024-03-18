from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)
jwt = JWTManager(app)


# User Model
class User(db.Model):
	id = db.Column(db.String, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(80), nullable=False)


# Post Model
class Post(db.Model):
	id = db.Column(db.String, primary_key=True)
	content = db.Column(db.String(280), nullable=False)
	user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)


# Routes
@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(id=str(uuid.uuid4()), username=data['username'], email=data['email'], password=generate_password_hash(data['password'], method='sha256'))
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'Registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if not user or not check_password_hash(user.password, data['password']):
		return jsonify({'message': 'Bad Login Info'}), 401
	access_token = create_access_token(identity=user.id)
	return jsonify(access_token=access_token), 200


@app.route('/post', methods=['POST'])
@jwt_required

def post():
	data = request.get_json()
	new_post = Post(id=str(uuid.uuid4()), content=data['content'], user_id=data['user_id'])
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created'}), 201


if __name__ == '__main__':
	app.run(debug=True)
