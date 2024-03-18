class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.notifications = []
		self.following = []
		self.followers = []
		self.posts = []
		self.private = False

	def receive_notification(self, notification):
		self.notifications.append(notification)

	def view_notifications(self):
		return self.notifications

	def authenticate(self, password):
		return self.password == password

	def reset_password(self, new_password):
		self.password = new_password

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def update_bio(self, bio):
		self.bio = bio

	def add_website_link(self, website):
		self.website_link = website

	def set_location(self, location):
		self.location = location

	def toggle_privacy(self):
		self.private = not self.private

	def follow(self, user):
		self.following.append(user)
		user.followers.append(self)

	def unfollow(self, user):
		self.following.remove(user)
		user.followers.remove(self)

	def post(self, post):
		self.posts.append(post)

	def view_timeline(self):
		timeline = []
		for user in self.following:
			timeline.extend(user.posts)
		return timeline

	def recommend_users(self, all_users):
		recommendations = []
		for user in all_users:
			if user != self and user not in self.following:
				mutual_followers = len(set(self.following) & set(user.followers))
				activity = len(user.posts)
				if mutual_followers > 0 or activity > 0:
					recommendations.append((user, mutual_followers * 2 + activity))
		recommendations.sort(key=lambda x: x[1], reverse=True)
		return [user for user, score in recommendations]
