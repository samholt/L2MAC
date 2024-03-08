import datetime

# Mock database
posts_db = {}


class Post:
	def __init__(self, post_id, user_id, content, timestamp):
		self.post_id = post_id
		self.user_id = user_id
		self.content = content
		self.timestamp = timestamp
		self.likes = 0
		self.retweets = 0
		self.replies = []


def create_post(user_id, content):
	# Generate a unique post_id
	post_id = len(posts_db) + 1
	timestamp = datetime.datetime.now()

	# Create a new post
	post = Post(post_id, user_id, content, timestamp)

	# Store the post in the database
	posts_db[post_id] = post

	return post_id

def delete_post(user_id, post_id):
	# Check if the post exists
	if post_id in posts_db:
		# Check if the user is the author of the post
		if posts_db[post_id].user_id == user_id:
			# Delete the post
			del posts_db[post_id]
			return True
	return False

def like_post(user_id, post_id):
	# Check if the post exists
	if post_id in posts_db:
		# Increment the likes count
		posts_db[post_id].likes += 1
		return True
	return False

def retweet_post(user_id, post_id):
	# Check if the post exists
	if post_id in posts_db:
		# Increment the retweets count
		posts_db[post_id].retweets += 1
		return True
	return False

def reply_to_post(user_id, post_id, content):
	# Check if the post exists
	if post_id in posts_db:
		# Add the reply to the replies list
		posts_db[post_id].replies.append((user_id, content))
		return True
	return False

def search_posts(keyword):
	return [post for post in posts_db.values() if keyword in post.content]
