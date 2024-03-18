class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website=None, location=None):
		self.email = email
		self.username = username
		self.password = password
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.following = []
		self.followers = []
		self.posts = []
		self.notifications = []

	def edit_profile(self, profile_picture, bio, website, location):
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		return 'Profile updated successfully'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting toggled'

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
			user.notifications.append(f'{self.username} started following you.')
			return 'Followed successfully'
		else:
			return 'Already following'

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)
			return 'Unfollowed successfully'
		else:
			return 'Not following'

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return timeline

	def like(self, post):
		post.likes.append(self)
		post.user.notifications.append(f'{self.username} liked your post.')
		return 'Post liked'

	def retweet(self, post):
		self.posts.append(post)
		post.user.notifications.append(f'{self.username} retweeted your post.')
		return 'Post retweeted'

	def reply(self, post, reply):
		post.replies.append((self, reply))
		post.user.notifications.append(f'{self.username} replied to your post.')
		return 'Reply posted'

# Mock database
users_db = {}

def register(email, username, password, is_private):
	if email in users_db or username in users_db:
		return 'User already exists'
	else:
		new_user = User(email, username, password, is_private)
		users_db[username] = new_user
		return new_user

def authenticate(username, password):
	if username in users_db and users_db[username].password == password:
		return 'User authenticated'
	else:
		return 'Authentication failed'

def reset_password(username, new_password):
	if username in users_db:
		users_db[username].password = new_password
		return 'Password reset successful'
	else:
		return 'User does not exist'

