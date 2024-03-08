class VotingSystem:
	def __init__(self, id, options=None):
		self.id = id
		self.options = options if options else []
		self.votes = {option: 0 for option in self.options}

	def create_voting_system(self, id, options):
		self.id = id
		self.options = options
		self.votes = {option: 0 for option in self.options}

	def add_option(self, option):
		if option not in self.options:
			self.options.append(option)
			self.votes[option] = 0

	def remove_option(self, option):
		if option in self.options:
			self.options.remove(option)
			del self.votes[option]

	def cast_vote(self, option):
		if option in self.options:
			self.votes[option] += 1

	def get_info(self):
		return {'id': self.id, 'options': self.options, 'votes': self.votes}
