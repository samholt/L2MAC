import datetime


class Message:
	def __init__(self):
		self.database = {}

	def send(self, sender, receiver, text):
		timestamp = datetime.datetime.now()
		if sender not in self.database:
			self.database[sender] = {}
		if receiver not in self.database[sender]:
			self.database[sender][receiver] = []
		self.database[sender][receiver].append((text, timestamp))

	def block(self, blocker, blockee):
		if blocker not in self.database:
			self.database[blocker] = {}
		self.database[blocker][blockee] = 'blocked'

