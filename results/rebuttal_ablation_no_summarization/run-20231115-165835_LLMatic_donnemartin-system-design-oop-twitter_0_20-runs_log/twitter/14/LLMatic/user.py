import jwt
import datetime


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None, visible=True):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.visible = visible
		self.following = []
		self.followers = []
		self.inbox = []
		self.posts = []

	def generate_auth_token(self):
		payload = {
			'sub': self.username,
			'iat': datetime.datetime.utcnow(),
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
		}
		return jwt.encode(payload, 'secret', algorithm='HS256')

	def verify_auth_token(self, token):
		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
			return payload['sub'] == self.username
		except jwt.ExpiredSignatureError:
			return False
		except jwt.InvalidTokenError:
			return False

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location

	def toggle_visibility(self):
		self.visible = not self.visible

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def timeline(self):
		timeline_posts = []
		for user in self.following:
			timeline_posts.extend(user.posts)
		return sorted(timeline_posts, key=lambda post: post.timestamp, reverse=True)

	@staticmethod
	def search_users(users, keyword):
		return [user for user in users if keyword in user.username or (user.bio and keyword in user.bio)]

	def recommend_users(self, users):
		recommendations = []
		for user in users:
			if user != self and user.visible:
				common_followers = len(set(self.followers) & set(user.followers))
				common_interests = len(set(self.bio.split()) & set(user.bio.split())) if self.bio and user.bio else 0
				activity = len(user.posts)
				if common_followers > 0 or common_interests > 0 or activity > 0:
					recommendations.append((user, common_followers, common_interests, activity))
		return sorted(recommendations, key=lambda x: (x[1], x[2], x[3]), reverse=True)
