class Post:
	def __init__(self, user, text, image=None):
		self.user = user
		self.text = text
		self.image = image
		self.likes = []
		self.replies = []
		self.user.posts.append(self)

# Mock database
post_db = {}

def create_post(user, text, image=None):
	if user.username in post_db:
		post_db[user.username].append(Post(user, text, image))
	else:
		post_db[user.username] = [Post(user, text, image)]
	return 'Post created successfully'
