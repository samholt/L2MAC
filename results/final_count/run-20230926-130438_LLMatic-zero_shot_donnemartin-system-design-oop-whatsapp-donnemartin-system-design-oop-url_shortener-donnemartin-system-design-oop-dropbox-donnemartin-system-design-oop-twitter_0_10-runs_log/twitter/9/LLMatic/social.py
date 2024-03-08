class Social:
	def __init__(self):
		self.followers = {}
		self.following = {}
		self.timeline = {}
		self.messages = {}
		self.blocked = {}
		self.notifications = {}

	def follow(self, follower, followee):
		if follower not in self.following:
			self.following[follower] = []
		self.following[follower].append(followee)
		if followee not in self.followers:
			self.followers[followee] = []
		self.followers[followee].append(follower)

	def unfollow(self, follower, followee):
		if follower in self.following and followee in self.following[follower]:
			self.following[follower].remove(followee)
		if followee in self.followers and follower in self.followers[followee]:
			self.followers[followee].remove(follower)

	def notify(self, followee):
		if followee in self.followers:
			return self.followers[followee]
		return []

	def view_timeline(self, user):
		if user in self.following:
			return self.following[user]
		return []

	def send_message(self, sender, receiver, message):
		if sender not in self.messages:
			self.messages[sender] = {}
		if receiver not in self.messages[sender]:
			self.messages[sender][receiver] = []
		self.messages[sender][receiver].append(message)

	def view_messages(self, viewer, viewed):
		if viewer in self.messages and viewed in self.messages[viewer]:
			return self.messages[viewer][viewed]
		return []

	def block_user(self, blocker, blocked):
		if blocker not in self.blocked:
			self.blocked[blocker] = []
		self.blocked[blocker].append(blocked)

	def unblock_user(self, unblocker, unblocked):
		if unblocker in self.blocked and unblocked in self.blocked[unblocker]:
			self.blocked[unblocker].remove(unblocked)

	def notify_like(self, liker, liked):
		if liked not in self.notifications:
			self.notifications[liked] = []
		self.notifications[liked].append(f'{liker} liked your post')

	def notify_retweet(self, retweeter, retweeted):
		if retweeted not in self.notifications:
			self.notifications[retweeted] = []
		self.notifications[retweeted].append(f'{retweeter} retweeted your post')

	def notify_reply(self, replier, replied):
		if replied not in self.notifications:
			self.notifications[replied] = []
		self.notifications[replied].append(f'{replier} replied to your post')

	def notify_mention(self, mentioner, mentioned):
		if mentioned not in self.notifications:
			self.notifications[mentioned] = []
		self.notifications[mentioned].append(f'{mentioner} mentioned you in a post')

	def view_notifications(self, user):
		if user in self.notifications:
			return self.notifications[user]
		return []
