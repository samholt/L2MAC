from models.user import User

users_db = {}

class UserService:
	@staticmethod
	def create_user(user: User):
		users_db[user.id] = user
		return user

	@staticmethod
	def get_user(user_id: str):
		return users_db.get(user_id)

	@staticmethod
	def update_user(user: User):
		users_db[user.id] = user
		return user

	@staticmethod
	def delete_user(user_id: str):
		if user_id in users_db:
			del users_db[user_id]
