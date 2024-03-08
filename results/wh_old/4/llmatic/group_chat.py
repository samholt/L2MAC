from chat import Chat


class GroupChat(Chat):
	def add_user(self, user_id):
		if user_id not in self.user_ids:
			self.user_ids.append(user_id)

	def remove_user(self, user_id):
		if user_id in self.user_ids:
			self.user_ids.remove(user_id)
