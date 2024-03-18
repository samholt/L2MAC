from flask import Flask, request
from post import Post
from user import User
from message import Message
from notification import Notification

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/post', methods=['POST'])
def create_post():
	title = request.form.get('title')
	content = request.form.get('content')
	user_id = request.form.get('user_id')
	Post.create_post(title, content, user_id)
	return 'Post created', 201

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	Post.delete_post(post_id)
	return 'Post deleted', 200

@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	Post.posts[post_id].like_post()
	return 'Post liked', 200

@app.route('/post/<int:post_id>/retweet', methods=['POST'])
def retweet_post(post_id):
	Post.posts[post_id].retweet_post()
	return 'Post retweeted', 200

@app.route('/post/<int:post_id>/reply', methods=['POST'])
def reply_post(post_id):
	reply = request.form.get('reply')
	Post.posts[post_id].reply_post(reply)
	return 'Reply added', 200

@app.route('/post/search', methods=['GET'])
def search_post():
	keyword = request.args.get('keyword')
	results = Post.search_posts(keyword)
	return {'results': [post.__dict__ for post in results]}, 200

@app.route('/post/trending', methods=['GET'])
def trending_topics():
	trending = Post.trending_topics()
	return {'trending': trending}, 200

@app.route('/user/<int:user_id>/recommend', methods=['GET'])
def recommend_users(user_id):
	recommended = User.users[user_id].recommend_users()
	return {'recommended': [user.__dict__ for user in recommended]}, 200

@app.route('/message', methods=['POST'])
def send_message():
	sender = request.form.get('sender')
	recipient = request.form.get('recipient')
	content = request.form.get('content')
	message = Message(sender, recipient, content)
	message.send_message()
	return 'Message sent', 200

@app.route('/notification', methods=['POST'])
def create_notification():
	user = request.form.get('user')
	notification_type = request.form.get('notification_type')
	notification = Notification(user, notification_type)
	notification.create_notification()
	return 'Notification created', 200

@app.route('/notification', methods=['GET'])
def view_notifications():
	user = request.args.get('user')
	notifications = user.view_notifications()
	return {'notifications': notifications}, 200

if __name__ == '__main__':
	app.run()
