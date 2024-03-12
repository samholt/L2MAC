from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, Post, Like, Retweet, Reply, Follow, db
import bcrypt


routes = Blueprint('routes', __name__)


@routes.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	email = request.json.get('email', None)
	password = request.json.get('password', None)

	if not username:
		return {'error': 'Username is required'}, 400
	if not email:
		return {'error': 'Email is required'}, 400
	if not password:
		return {'error': 'Password is required'}, 400

	password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

	new_user = User(username=username, email=email, password=password_hash)
	db.session.add(new_user)
	db.session.commit()

	return {'message': 'User created'}, 201


@routes.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', None)
	password = request.json.get('password', None)

	if not username:
		return {'error': 'Username is required'}, 400
	if not password:
		return {'error': 'Password is required'}, 400

	user = User.query.filter_by(username=username).first()

	if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
		access_token = create_access_token(identity=username)
		return {'access_token': access_token}, 200

	return {'error': 'Invalid username or password'}, 401


@routes.route('/edit_profile', methods=['PUT'])
@jwt_required()
def edit_profile():
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	user.profile_picture = request.json.get('profile_picture', user.profile_picture)
	user.bio = request.json.get('bio', user.bio)
	user.website_link = request.json.get('website_link', user.website_link)
	user.location = request.json.get('location', user.location)

	db.session.commit()

	return {'message': 'Profile updated'}, 200


@routes.route('/toggle_visibility', methods=['PUT'])
@jwt_required()
def toggle_visibility():
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	user.is_public = not user.is_public
	db.session.commit()

	return {'message': 'Profile visibility toggled'}, 200


@routes.route('/create_post', methods=['POST'])
@jwt_required()
def create_post():
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	content = request.json.get('content', None)
	images = request.json.get('images', None)

	if not content:
		return {'error': 'Content is required'}, 400

	new_post = Post(content=content, images=images, user_id=user.id)
	db.session.add(new_post)
	db.session.commit()

	return {'message': 'Post created'}, 201


@routes.route('/delete_post/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	post = Post.query.get(post_id)

	if not post or post.user_id != user.id:
		return {'error': 'Post not found'}, 404

	db.session.delete(post)
	db.session.commit()

	return {'message': 'Post deleted'}, 200


@routes.route('/view_posts', methods=['GET'])
def view_posts():
	posts = Post.query.all()
	return {'posts': [post.content for post in posts]}, 200


@routes.route('/search_posts', methods=['GET'])
def search_posts():
	keyword = request.args.get('keyword', '')
	posts = Post.query.filter(Post.content.like('%' + keyword + '%')).all()
	return {'posts': [post.content for post in posts]}, 200


@routes.route('/like_post/<int:post_id>', methods=['POST'])
@jwt_required()
def like_post(post_id):
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	post = Post.query.get(post_id)

	if not post:
		return {'error': 'Post not found'}, 404

	like = Like(user_id=user.id, post_id=post.id)
	db.session.add(like)
	db.session.commit()

	return {'message': 'Post liked'}, 200


@routes.route('/retweet_post/<int:post_id>', methods=['POST'])
@jwt_required()
def retweet_post(post_id):
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	post = Post.query.get(post_id)

	if not post:
		return {'error': 'Post not found'}, 404

	retweet = Retweet(user_id=user.id, post_id=post.id)
	db.session.add(retweet)
	db.session.commit()

	return {'message': 'Post retweeted'}, 200


@routes.route('/reply_post/<int:post_id>', methods=['POST'])
@jwt_required()
def reply_post(post_id):
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	post = Post.query.get(post_id)

	if not post:
		return {'error': 'Post not found'}, 404

	content = request.json.get('content', None)

	if not content:
		return {'error': 'Content is required'}, 400

	reply = Reply(content=content, user_id=user.id, post_id=post.id)
	db.session.add(reply)
	db.session.commit()

	return {'message': 'Reply posted'}, 200


@routes.route('/view_interactions/<int:post_id>', methods=['GET'])
def view_interactions(post_id):
	post = Post.query.get(post_id)

	if not post:
		return {'error': 'Post not found'}, 404

	likes = Like.query.filter_by(post_id=post.id).count()
	retweets = Retweet.query.filter_by(post_id=post.id).count()
	replies = Reply.query.filter_by(post_id=post.id).all()

	return {'likes': likes, 'retweets': retweets, 'replies': [reply.content for reply in replies]}, 200


@routes.route('/follow_user/<int:user_id>', methods=['POST'])
@jwt_required()
def follow_user(user_id):
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	followed_user = User.query.get(user_id)

	if not followed_user:
		return {'error': 'User to follow not found'}, 404

	follow = Follow(follower_id=user.id, followed_id=followed_user.id)
	db.session.add(follow)
	db.session.commit()

	return {'message': 'User followed'}, 200


@routes.route('/unfollow_user/<int:user_id>', methods=['POST'])
@jwt_required()
def unfollow_user(user_id):
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	followed_user = User.query.get(user_id)

	if not followed_user:
		return {'error': 'User to unfollow not found'}, 404

	follow = Follow.query.filter_by(follower_id=user.id, followed_id=followed_user.id).first()

	if not follow:
		return {'error': 'Follow not found'}, 404

	db.session.delete(follow)
	db.session.commit()

	return {'message': 'User unfollowed'}, 200


@routes.route('/view_followers/<int:user_id>', methods=['GET'])
def view_followers(user_id):
	user = User.query.get(user_id)

	if not user:
		return {'error': 'User not found'}, 404

	followers = [follower.username for follower in user.followers]

	return {'followers': followers}, 200


@routes.route('/view_following/<int:user_id>', methods=['GET'])
def view_following(user_id):
	user = User.query.get(user_id)

	if not user:
		return {'error': 'User not found'}, 404

	following = [followed.username for followed in user.following]

	return {'following': following}, 200


@routes.route('/view_timeline', methods=['GET'])
@jwt_required()
def view_timeline():
	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	if not user:
		return {'error': 'User not found'}, 404

	following_ids = [followed.id for followed in user.following]
	posts = Post.query.filter(Post.user_id.in_(following_ids)).all()

	return {'posts': [post.content for post in posts]}, 200
