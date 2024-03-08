from models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
	@staticmethod
	def register(data):
		user = User(username=data['username'], email=data['email'], password=generate_password_hash(data['password']))
		user.save()
		return user

	@staticmethod
	def login(data):
		user = User.query.get(data['username'])
		if user and check_password_hash(user.password, data['password']):
			return user
		return None

	@staticmethod
	def get_user(username):
		return User.query.get(username)

	@staticmethod
	def update_user(username, data):
		user = User.query.get(username)
		if 'email' in data:
			user.email = data['email']
		if 'password' in data:
			user.password = generate_password_hash(data['password'])
		user.save()
		return user

class PostService:
	@staticmethod
	def create_post(data):
		post = Post(username=data['username'], content=data['content'])
		post.save()
		return post

	@staticmethod
	def get_post(post_id):
		return Post.query.get(post_id)

	@staticmethod
	def delete_post(post_id):
		post = Post.query.get(post_id)
		if post:
			post.delete()
