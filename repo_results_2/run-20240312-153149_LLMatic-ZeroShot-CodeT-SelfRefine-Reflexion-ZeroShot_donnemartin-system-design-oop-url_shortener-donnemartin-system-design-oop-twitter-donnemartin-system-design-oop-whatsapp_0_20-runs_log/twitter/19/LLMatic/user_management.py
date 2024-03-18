class User:
	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password = password
		self.is_authenticated = False
		self.profile_picture = None
		self.bio = ''
		self.website_link = None
		self.location = None
		self.is_profile_public = True
		self.followers = []
		self.following = []
		self.posts = []
		self.blocked_users = []
		self.messages = []
		self.notifications = []

	users_db = {}

	def register(self):
		self.users_db[self.username] = {'email': self.email, 'password': self.password, 'profile_picture': self.profile_picture, 'bio': self.bio, 'website_link': self.website_link, 'location': self.location, 'is_profile_public': self.is_profile_public, 'followers': self.followers, 'following': self.following, 'posts': self.posts, 'blocked_users': self.blocked_users, 'messages': self.messages, 'notifications': self.notifications}
		return 'User registered successfully'

	def authenticate(self, username, password):
		if self.users_db.get(username) and self.users_db[username]['password'] == password:
			self.is_authenticated = True
			return 'User authenticated successfully'
		else:
			return 'Invalid username or password'

	def reset_password(self, new_password):
		if self.is_authenticated:
			self.users_db[self.username]['password'] = new_password
			return 'Password reset successfully'
		else:
			return 'User not authenticated'

	def edit_profile(self, profile_picture, bio, website_link, location):
		if self.is_authenticated:
			self.users_db[self.username]['profile_picture'] = profile_picture
			self.users_db[self.username]['bio'] = bio
			self.users_db[self.username]['website_link'] = website_link
			self.users_db[self.username]['location'] = location
			return 'Profile updated successfully'
		else:
			return 'User not authenticated'

	def toggle_profile_visibility(self):
		if self.is_authenticated:
			self.users_db[self.username]['is_profile_public'] = not self.users_db[self.username]['is_profile_public']
			return 'Profile visibility toggled'
		else:
			return 'User not authenticated'

	def search(self, keyword):
		return keyword in self.username or keyword in self.bio

	def follow(self, user_to_follow):
		if user_to_follow in self.users_db and user_to_follow != self.username:
			self.users_db[self.username]['following'].append(user_to_follow)
			self.users_db[user_to_follow]['followers'].append(self.username)
			return 'Followed ' + user_to_follow
		else:
			return 'Cannot follow user'

	def unfollow(self, user_to_unfollow):
		if user_to_unfollow in self.users_db and user_to_unfollow in self.users_db[self.username]['following']:
			self.users_db[self.username]['following'].remove(user_to_unfollow)
			self.users_db[user_to_unfollow]['followers'].remove(self.username)
			return 'Unfollowed ' + user_to_unfollow
		else:
			return 'Cannot unfollow user'

	def get_timeline(self):
		timeline = []
		for user in self.users_db[self.username]['following']:
			timeline.extend(self.users_db[user]['posts'])
		return timeline

	def get_followers(self):
		return self.users_db[self.username]['followers']

	def get_following(self):
		return self.users_db[self.username]['following']

	def post(self, content):
		self.users_db[self.username]['posts'].append(content)
		return 'Post created'

	def block_user(self, user_to_block):
		if user_to_block in self.users_db and user_to_block != self.username:
			self.users_db[self.username]['blocked_users'].append(user_to_block)
			return 'Blocked ' + user_to_block
		else:
			return 'Cannot block user'

	def unblock_user(self, user_to_unblock):
		if user_to_unblock in self.users_db and user_to_unblock in self.users_db[self.username]['blocked_users']:
			self.users_db[self.username]['blocked_users'].remove(user_to_unblock)
			return 'Unblocked ' + user_to_unblock
		else:
			return 'Cannot unblock user'

	def send_message(self, receiver, content):
		if receiver in self.users_db and receiver not in self.users_db[self.username]['blocked_users']:
			self.users_db[self.username]['messages'].append({'receiver': receiver, 'content': content})
			self.users_db[receiver]['messages'].append({'sender': self.username, 'content': content})
			return 'Message sent'
		else:
			return 'Cannot send message'

	def add_notification(self, notification):
		self.users_db[self.username]['notifications'].append(notification)
		return 'Notification added'

	def remove_notification(self, notification):
		if notification in self.users_db[self.username]['notifications']:
			self.users_db[self.username]['notifications'].remove(notification)
			return 'Notification removed'
		else:
			return 'Notification not found'

	def get_notifications(self):
		return self.users_db[self.username]['notifications']
