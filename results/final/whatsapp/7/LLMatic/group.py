class Group:
	def __init__(self, name, picture, participants, admins, messages):
		self.name = name
		self.picture = picture
		self.participants = participants
		self.admins = admins
		self.messages = messages

	def create(self, name, picture):
		self.name = name
		self.picture = picture
		self.participants = []
		self.admins = []
		self.messages = []

	def add_participant(self, participant):
		self.participants.append(participant)

	def remove_participant(self, participant):
		self.participants.remove(participant)

	def assign_admin_role(self, participant):
		self.admins.append(participant)

	def remove_admin_role(self, participant):
		self.admins.remove(participant)

	def send_message(self, message):
		self.messages.append(message)

	def receive_message(self, message):
		self.messages.append(message)

	def read_message(self, message):
		return message in self.messages

	def share_image(self, image):
		self.messages.append(image)

	def send_emoji(self, emoji):
		self.messages.append(emoji)
