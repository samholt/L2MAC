from models import Post, User, Message
from collections import Counter
import itertools

mock_db = {'users': [User(1, 'user1', 'user1@example.com', 'password1'), User(2, 'user2', 'user2@example.com', 'password2')], 'posts': [], 'messages': []}


def create_post(user_id, content):
	new_post = Post(len(mock_db['posts']) + 1, user_id, content)
	mock_db['posts'].append(new_post)
	return new_post


def delete_post(user_id, post_id):
	for post in mock_db['posts']:
		if post.id == post_id and post.user_id == user_id:
			mock_db['posts'].remove(post)
			return True
	return False


def like_post(user_id, post_id):
	for post in mock_db['posts']:
		if post.id == post_id:
			post.likes += 1
			return post
	return False


def retweet_post(user_id, post_id):
	for post in mock_db['posts']:
		if post.id == post_id:
			post.retweets += 1
			return post
	return False


def reply_to_post(user_id, post_id, reply_content):
	for post in mock_db['posts']:
		if post.id == post_id:
			post.replies.append({'user_id': user_id, 'content': reply_content})
			return post
	return False


def search_posts(keyword):
	results = []
	for post in mock_db['posts']:
		if keyword in post.content:
			results.append(post)
	return results


def search_users(username):
	results = []
	for user in mock_db['users']:
		if username == user.username:
			results.append(user)
	return results


def follow_user(user_id, target_user_id):
	for user in mock_db['users']:
		if user.id == user_id:
			for target_user in mock_db['users']:
				if target_user.id == target_user_id:
					user.following.append(target_user_id)
					target_user.followers.append(user_id)
					return True
	return False


def unfollow_user(user_id, target_user_id):
	for user in mock_db['users']:
		if user.id == user_id:
			for target_user in mock_db['users']:
				if target_user.id == target_user_id:
					user.following.remove(target_user_id)
					target_user.followers.remove(user_id)
					return True
	return False


def send_message(sender_id, receiver_id, content):
	new_message = Message(len(mock_db['messages']) + 1, sender_id, receiver_id, content)
	mock_db['messages'].append(new_message)
	return new_message


def get_notifications(user_id):
	for user in mock_db['users']:
		if user.id == user_id:
			return {'following': user.following, 'followers': user.followers}
	return None


def get_trending_topics():
	topics = [post.content.split() for post in mock_db['posts']]
	topics = list(itertools.chain(*topics))
	counter = Counter(topics)
	return counter.most_common(10)


def get_user_recommendations(user_id):
	for user in mock_db['users']:
		if user.id == user_id:
			mutual_followers = [u for u in mock_db['users'] if set(user.following).intersection(set(u.following))]
			return mutual_followers
	return None
