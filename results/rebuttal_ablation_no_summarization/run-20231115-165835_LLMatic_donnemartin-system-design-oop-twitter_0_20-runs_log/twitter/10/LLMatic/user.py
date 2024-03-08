import jwt
import datetime


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None, private=False):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.private = private
		self.following = []
		self.followers = []
		self.notifications = []
		self.messages = []
		self.blocked_users = []
		self.posts = []

	# Mock database
	users = {}

	def register(self):
		User.users[self.username] = {'email': self.email, 'password': self.password, 'profile_picture': self.profile_picture, 'bio': self.bio, 'website_link': self.website_link, 'location': self.location, 'private': self.private, 'following': self.following, 'followers': self.followers, 'notifications': self.notifications, 'messages': self.messages, 'blocked_users': self.blocked_users, 'posts': self.posts, 'username': self.username}
		return User.users

	def authenticate(self, username, password):
		if User.users.get(username) and User.users[username]['password'] == password:
			token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret')
			return token
		else:
			return 'Invalid username or password'

	def reset_password(self, username, new_password):
		if User.users.get(username):
			User.users[username]['password'] = new_password
			return 'Password reset successful'
		else:
			return 'User not found'

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location
		return 'Profile updated successfully'

	def toggle_privacy(self):
		self.private = not self.private
		return 'Privacy setting updated successfully'

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
		return sorted(timeline, key=lambda post: post['timestamp'], reverse=True)

	def view_notifications(self):
		return self.notifications

	def recommend_users(self):
		# Recommend users based on mutual followers
		mutual_followers = [user for user in User.users.values() if len(set(self.followers) & set(user['followers'])) > 0]

		# Recommend users based on similar interests (bio)
		similar_interests = [user for user in User.users.values() if self.bio and user['bio'] and len(set(self.bio.split()) & set(user['bio'].split())) > 0]

		# Recommend users based on activity (number of posts)
		active_users = sorted(User.users.values(), key=lambda user: len(user['posts']), reverse=True)[:10]

		# Combine recommendations and remove duplicates
		recommendations = list({user['username']: user for user in mutual_followers + similar_interests + active_users}.values())

		# Remove users that the current user is already following or has blocked
		recommendations = [user for user in recommendations if user['username'] not in self.following and user['username'] not in self.blocked_users]

		return recommendations
