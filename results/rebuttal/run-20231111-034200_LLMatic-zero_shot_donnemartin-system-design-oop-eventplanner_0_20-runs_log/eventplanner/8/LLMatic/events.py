class Event:
	def __init__(self, id, name, date, location):
		self.id = id
		self.name = name
		self.date = date
		self.location = location

	def update_event(self, name, date, location):
		self.name = name
		self.date = date
		self.location = location

	def view_event(self):
		return {'id': self.id, 'name': self.name, 'date': self.date, 'location': self.location}
