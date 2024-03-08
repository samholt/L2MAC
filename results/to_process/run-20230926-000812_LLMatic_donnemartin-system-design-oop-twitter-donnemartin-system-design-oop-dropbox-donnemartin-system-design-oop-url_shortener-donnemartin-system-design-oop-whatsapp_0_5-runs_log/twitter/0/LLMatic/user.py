import bcrypt
import jwt


class User:
	def __init__(self, email, username, password, is_private, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		self.is_private = is_private
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = set()
		self.followers = set()
		self.timeline = []
		self.inbox = []
		self.blocked_users = []
		self.notifications = []

	def authenticate(self, password):
		return bcrypt.checkpw(password.encode(), self.password)

	def reset_password(self, new_password):
		self.password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())

	def generate_auth_token(self):
		payload = {'username': self.username}
		return jwt.encode(payload, 'secret', algorithm='HS256')

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location

	def toggle_privacy(self):
		self.is_private = not self.is_private

	def follow(self, user):
		if user not in self.following:
			self.following.add(user)
			user.followers.add(self)
			user.notify_new_follower(self.username)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def notify_new_follower(self, username):
		self.notifications.append(f'{username} started following you.')

	def notify_like(self, post):
		self.notifications.append(f'Your post {post} got a new like.')

	def notify_retweet(self, post):
		self.notifications.append(f'Your post {post} was retweeted.')

	def notify_reply(self, post):
		self.notifications.append(f'Your post {post} got a new reply.')

	def notify_mention(self, post):
		self.notifications.append(f'You were mentioned in a post {post}.')

	def view_timeline(self):
		return self.timeline

	def update_timeline(self, post):
		self.timeline.append(post)
		for follower in self.followers:
			follower.timeline.append(post)

	def block_user(self, user):
		self.blocked_users.append(user)
		return f'{user.username} has been blocked.'

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
			return f'{user.username} has been unblocked.'
		else:
			return f'{user.username} is not blocked.'

	def recommend_users(self, users):
		recommendations = []
		for user in users:
			if user not in self.following and user not in self.blocked_users:
				mutual_followers = len(self.followers.intersection(user.followers))
				if mutual_followers > 0 or len(user.timeline) > 0:
					recommendations.append(user)
		return recommendations

