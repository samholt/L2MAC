class SocialInteraction:
	def __init__(self):
		self.followers = {}
		self.following = {}
		self.posts = {}
		self.conversations = {}
		self.blocked_users = {}
		self.notifications = {}

	def follow(self, follower, followee):
		if follower not in self.following:
			self.following[follower] = set()
		self.following[follower].add(followee)

		if followee not in self.followers:
			self.followers[followee] = set()
		self.followers[followee].add(follower)

	def unfollow(self, follower, followee):
		if follower in self.following and followee in self.following[follower]:
			self.following[follower].remove(followee)
		if followee in self.followers and follower in self.followers[followee]:
			self.followers[followee].remove(follower)

	def get_timeline(self, user):
		timeline = []
		if user in self.following:
			for followee in self.following[user]:
				if followee in self.posts:
					timeline.extend(self.posts[followee])
		return sorted(timeline, key=lambda x: x['timestamp'], reverse=True)

	def notify_followers(self, user, post):
		if user not in self.posts:
			self.posts[user] = []
		self.posts[user].append(post)
		if user in self.followers:
			for follower in self.followers[user]:
				print(f'New post from {user}!')

	def create_conversation(self, user1, user2):
		self.conversations[(user1, user2)] = []

	def send_message(self, sender, receiver, message):
		if (sender, receiver) in self.conversations:
			self.conversations[(sender, receiver)].append({'sender': sender, 'timestamp': message['timestamp'], 'content': message['content']})
		elif (receiver, sender) in self.conversations:
			self.conversations[(receiver, sender)].append({'sender': sender, 'timestamp': message['timestamp'], 'content': message['content']})

	def get_conversation(self, user1, user2):
		if (user1, user2) in self.conversations:
			return self.conversations[(user1, user2)]
		elif (user2, user1) in self.conversations:
			return self.conversations[(user2, user1)]
		else:
			return None

	def block_user(self, user, blocked_user):
		if user not in self.blocked_users:
			self.blocked_users[user] = set()
		self.blocked_users[user].add(blocked_user)

	def unblock_user(self, user, blocked_user):
		if user in self.blocked_users and blocked_user in self.blocked_users[user]:
			self.blocked_users[user].remove(blocked_user)

	def is_blocked(self, user, blocked_user):
		return user in self.blocked_users and blocked_user in self.blocked_users[user]

	def notify(self, user, notification):
		if user not in self.notifications:
			self.notifications[user] = []
		self.notifications[user].append(notification)

	def like(self, user, post):
		self.notify(post['user'], {'type': 'like', 'user': user, 'post': post})

	def retweet(self, user, post):
		self.notify(post['user'], {'type': 'retweet', 'user': user, 'post': post})

	def reply(self, user, post, reply):
		self.notify(post['user'], {'type': 'reply', 'user': user, 'post': post, 'reply': reply})

	def mention(self, user, post, mentioned):
		self.notify(mentioned, {'type': 'mention', 'user': user, 'post': post})
