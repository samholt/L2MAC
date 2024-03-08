import jwt
import datetime

SECRET_KEY = 'SECRET'


class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = password
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.followers = []

	def register(self):
		# In a real-world application, this method would save the user to a database
		# Here we just return a success message
		return 'User registered successfully'

	def authenticate(self, password):
		if self.password == password:
			token = jwt.encode({'user': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		else:
			return 'Invalid password'

	def reset_password(self, new_password):
		self.password = new_password
		return 'Password reset successfully'

	def update_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location
		return 'Profile updated successfully'

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return 'Privacy setting toggled'

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)
			user.notify_new_follower(self)
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

	def notify_new_follower(self, follower):
		return f'New follower: {follower.username}'

	def notify_like(self, post):
		return f'Your post was liked: {post.id}'

	def notify_retweet(self, post):
		return f'Your post was retweeted: {post.id}'

	def notify_reply(self, post):
		return f'You received a reply on your post: {post.id}'

	def notify_mention(self, post):
		return f'You were mentioned in a post: {post.id}'

	def recommend_users(self):
		# In a real-world application, this method would recommend users based on interests, activity, and mutual followers
		# Here we just return a placeholder message
		return 'Recommended users'
