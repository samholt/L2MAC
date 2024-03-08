class Post:
	def __init__(self, id, user_id, content, image=None, likes=0, retweets=0, replies=None):
		self.id = id
		self.user_id = user_id
		self.content = content
		self.image = image
		self.likes = likes
		self.retweets = retweets
		self.replies = replies if replies else []

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, user_id, content):
		reply_id = len(self.replies) + 1
		reply = Post(reply_id, user_id, content)
		self.replies.append(reply)

# Mock database
posts_db = {}

# Function to create a new post
def create_post(user_id, content):
	# Generate a unique post id
	post_id = len(posts_db) + 1
	# Create a new post instance
	post = Post(post_id, user_id, content)
	# Store the post in the mock database
	posts_db[post_id] = post
	return True

def search_posts(keyword):
	return [post for post in posts_db.values() if keyword in post.content]

def get_trending_topics():
	# Sort the posts in the mock database by the sum of likes and retweets
	trending_posts = sorted(posts_db.values(), key=lambda post: post.likes + post.retweets, reverse=True)
	return trending_posts
