from flask import Flask, request, jsonify
from database import db
from user import User
from post import Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and user.password == data['password']:
		return jsonify(user.to_dict()), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	post = Post(**data)
	db.session.add(post)
	db.session.commit()
	return jsonify(post.to_dict()), 201

@app.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
	post = Post.query.get(post_id)
	if post:
		return jsonify(post.to_dict()), 200
	return {'message': 'Post not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
