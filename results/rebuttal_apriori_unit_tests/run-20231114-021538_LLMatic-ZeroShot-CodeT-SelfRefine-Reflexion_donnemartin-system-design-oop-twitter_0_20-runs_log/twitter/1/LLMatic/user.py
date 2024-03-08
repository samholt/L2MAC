class User:
	def __init__(self, id, username, email, password, profile_picture=None, bio=None, website_link=None, location=None, is_private=False):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.is_private = is_private
		self.following = set()

	def edit_profile(self, bio, website_link, location):
		self.bio = bio
		self.website_link = website_link
		self.location = location
		return True

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return True

	def follow_user(self, target_user_id):
		self.following.add(target_user_id)
		return True

	def unfollow_user(self, target_user_id):
		if target_user_id in self.following:
			self.following.remove(target_user_id)
			return True
		return False

mock_db = {}


def register_user(username, email, password):
	if email in mock_db:
		return False
	user_id = len(mock_db) + 1
	mock_db[email] = User(user_id, username, email, password)
	return True


def authenticate_user(email, password):
	if email in mock_db and mock_db[email].password == password:
		return True
	return False

def edit_profile(email, bio, website_link, location):
	if email in mock_db:
		return mock_db[email].edit_profile(bio, website_link, location)
	return False

def toggle_privacy(email):
	if email in mock_db:
		return mock_db[email].toggle_privacy()
	return False

def follow_user(email, target_user_id):
	if email in mock_db:
		return mock_db[email].follow_user(target_user_id)
	return False

def unfollow_user(email, target_user_id):
	if email in mock_db:
		return mock_db[email].unfollow_user(target_user_id)
	return False

def search_users(username):
	return [user for user in mock_db.values() if user.username == username]

def get_user_recommendations(user_id):
	if user_id not in [user.id for user in mock_db.values()]:
		return None
	user = [user for user in mock_db.values() if user.id == user_id][0]
	common_following = [other_user for other_user in mock_db.values() if other_user.id != user_id and user.following & other_user.following]
	return common_following
