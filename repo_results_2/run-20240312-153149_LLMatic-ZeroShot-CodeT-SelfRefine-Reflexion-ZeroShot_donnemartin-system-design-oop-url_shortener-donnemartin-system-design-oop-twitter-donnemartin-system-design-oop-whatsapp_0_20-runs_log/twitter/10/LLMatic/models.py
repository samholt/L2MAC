import datetime

class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None, is_private=False):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.is_private = is_private
		self.following = []
		self.followers = []
		self.posts = []
		self.blocked = []
		self.messages = []

	def check_password(self, password):
		return self.password == password

	def send_password_reset_email(self):
		print(f'Sending password reset email to {self.email}')

	def check_password_reset_token(self, token):
		return token == 'reset'

	def reset_password(self, new_password):
		self.password = new_password

	def update_profile(self, profile_picture=None, bio=None, website_link=None, location=None, is_private=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location
		if is_private is not None:
			self.is_private = is_private

	def get_profile(self):
		if self.is_private:
			return {'message': 'This profile is private'}
		return {
			'email': self.email,
			'username': self.username,
			'profile_picture': self.profile_picture,
			'bio': self.bio,
			'website_link': self.website_link,
			'location': self.location
		}

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def get_following_posts(self):
		return [post for user in self.following for post in user.posts]

	def block(self, user):
		if user not in self.blocked:
			self.blocked.append(user)

	def unblock(self, user):
		if user in self.blocked:
			self.blocked.remove(user)

	def send_message(self, recipient, content):
		if recipient in self.blocked:
			return {'message': 'This user has blocked you'}
		message = Message(self, recipient, content)
		self.messages.append(message)
		recipient.messages.append(message)
		return {'message': 'Message sent successfully'}

	def get_messages(self):
		return [{'sender': message.sender.username, 'recipient': message.recipient.username, 'content': message.content, 'sent_at': message.sent_at} for message in self.messages]

class Post:
	id_counter = 1

	def __init__(self, user, content):
		self.id = Post.id_counter
		Post.id_counter += 1
		self.user = user
		self.content = content
		self.created_at = datetime.datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.hashtags = [word for word in content.split() if word.startswith('#')]

	def delete(self):
		self.user = None
		self.content = None
		self.created_at = None
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.hashtags = []

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, user, content):
		self.replies.append({'user': user, 'content': content})

class Message:
	def __init__(self, sender, recipient, content):
		self.sender = sender
		self.recipient = recipient
		self.content = content
		self.sent_at = datetime.datetime.now()

