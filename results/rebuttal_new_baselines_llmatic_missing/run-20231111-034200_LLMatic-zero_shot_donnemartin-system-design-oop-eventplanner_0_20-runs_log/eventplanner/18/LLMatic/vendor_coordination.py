class Vendor:
	def __init__(self, name, service_type, reviews):
		self.name = name
		self.service_type = service_type
		self.reviews = reviews

	def view_profile(self):
		return {'name': self.name, 'service_type': self.service_type, 'reviews': self.reviews}

	@staticmethod
	def compare_vendors(vendor1, vendor2):
		return vendor1.view_profile(), vendor2.view_profile()


class MessagingSystem:
	def __init__(self):
		self.messages = {}

	def send_message(self, sender, receiver, message):
		if receiver not in self.messages:
			self.messages[receiver] = []
		self.messages[receiver].append({'from': sender, 'message': message})

	def view_messages(self, receiver):
		return self.messages.get(receiver, [])
