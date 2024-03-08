from user import mock_db as user_db
from post import posts_db
from message import mock_db as message_db

def get_notifications(email):
	# Get the user's following list
	following = user_db[email].following
	# Get posts from the users that the current user is following
	posts = [post for post in posts_db.values() if post.user_id in following]
	# Get messages where the current user is the receiver
	messages = [message for message in message_db.values() if message.receiver_id == user_db[email].id]
	# Return the posts and messages
	return posts, messages
