from models.user import User


class UserController:
	def __init__(self):
		self.users = []

	def create_user(self, username: str, password: str):
		user = User(username, password, [], [])
		self.users.append(user)
		return user

	def get_user(self, username: str):
		for user in self.users:
			if user.username == username:
				return user
		return None

	def update_password(self, username: str, new_password: str):
		user = self.get_user(username)
		if user:
			user.password = new_password
			return user
		return None

	def delete_user(self, username: str):
		user = self.get_user(username)
		if user:
			self.users.remove(user)
			return user
		return None

	def follow_user(self, follower_username: str, followee_username: str):
		follower = self.get_user(follower_username)
		followee = self.get_user(followee_username)
		if follower and followee:
			follower.following.append(followee)
			followee.followers.append(follower)
			return True
		return False
