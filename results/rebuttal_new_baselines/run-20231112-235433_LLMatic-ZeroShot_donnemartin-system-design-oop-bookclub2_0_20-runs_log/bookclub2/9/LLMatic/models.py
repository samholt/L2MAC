class User:
	def __init__(self, id, username, email, password, role):
		self.id = id
		self.username = username
		self.email = email
		self.password = password
		self.role = role


class BookClub:
	def __init__(self, id, name, description, privacy, members):
		self.id = id
		self.name = name
		self.description = description
		self.privacy = privacy
		self.members = members

	def add_member(self, user):
		self.members.append(user)

	def remove_member(self, user):
		self.members.remove(user)

	def update_privacy(self, privacy):
		self.privacy = privacy

	def update_description(self, description):
		self.description = description


class Meeting:
	def __init__(self, id, date, time, location, agenda):
		self.id = id
		self.date = date
		self.time = time
		self.location = location
		self.agenda = agenda


class Discussion:
	def __init__(self, id, topic, comments, votes):
		self.id = id
		self.topic = topic
		self.comments = comments
		self.votes = votes
