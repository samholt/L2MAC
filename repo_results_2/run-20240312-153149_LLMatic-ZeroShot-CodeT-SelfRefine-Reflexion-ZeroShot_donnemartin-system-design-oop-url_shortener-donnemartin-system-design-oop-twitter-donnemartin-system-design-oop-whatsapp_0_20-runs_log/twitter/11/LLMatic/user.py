import jwt
import datetime

SECRET_KEY = 'SECRET'

class User:
	def __init__(self, email, username, password, is_private):
		self.email = email
		self.username = username
		self.password = password
		self.is_private = is_private
		self.profile_picture = None
		self.bio = None
		self.website_link = None
		self.location = None
		self.following = set()
		self.followers = set()
		self.notifications = []

	def register(self):
		return self

	def authenticate(self, password):
		if self.password == password:
			token = jwt.encode({'user': self.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		else:
			return False

	def reset_password(self, new_password):
		self.password = new_password
		return True

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_bio(self, bio):
		self.bio = bio

	def set_website_link(self, link):
		self.website_link = link

	def set_location(self, location):
		self.location = location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def follow(self, user):
		if user.is_private:
			return 'Request sent'
		self.following.add(user)
		user.followers.add(self)
		user.notifications.append(f'{self.username} started following you.')
		return 'Followed'

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)
		return 'Unfollowed'

	def view_timeline(self):
		return [user.username for user in self.following]

	def notify_like(self, post):
		post.user.notifications.append(f'{self.username} liked your post: {post.text}')

	def notify_retweet(self, post):
		post.user.notifications.append(f'{self.username} retweeted your post: {post.text}')

	def notify_reply(self, post, reply):
		post.user.notifications.append(f'{self.username} replied to your post: {post.text} with {reply.text}')

	def notify_mention(self, post):
		for user in post.mentions:
			user.notifications.append(f'{self.username} mentioned you in a post: {post.text}')

	def recommend_users(self, users):
		recommended_users = set()
		for user in users:
			if user != self and user not in self.following:
				mutual_following = self.following.intersection(user.following)
				if len(mutual_following) > 0:
					recommended_users.add(user)
		return list(recommended_users)

