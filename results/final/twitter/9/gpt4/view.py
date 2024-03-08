class View:
	def __init__(self, controller):
		self.controller = controller

	def display_user(self, user):
		print(f'User: {user.username}')
		print(f'Following: {[u.username for u in user.following]}')
		print(f'Followers: {[u.username for u in user.followers]}')
		print(f'Tweets: {[t.content for t in user.tweets]}')

	def display_tweet(self, tweet):
		print(f'Tweet: {tweet.content}')
		print(f'By: {tweet.user.username}')
		print(f'Privacy: {tweet.privacy}')
		print(f'Replies: {[r.content for r in tweet.replies]}')
		print(f'Mentions: {[m.username for m in tweet.mentions]}')

	def display_direct_message(self, dm):
		print(f'Direct Message: {dm.message}')
		print(f'From: {dm.sender.username}')
		print(f'To: {dm.receiver.username}')

	def display_mention(self, mention):
		print(f'Mention: {mention.user.username} in tweet {mention.tweet.content}')
