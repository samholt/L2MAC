class Discussion:
	forums = {}
	votes = {}

	def create_forum(self, club_id):
		if not club_id:
			raise ValueError('Missing required parameters')
		self.__class__.forums[club_id] = []

	def add_comment(self, club_id, user_id, comment):
		if not club_id or not user_id or not comment:
			raise ValueError('Missing required parameters')
		self.__class__.forums[club_id].append({'user_id': user_id, 'comment': comment})

	def vote_for_next_book(self, club_id, user_id, book_id):
		if not club_id or not user_id or not book_id:
			raise ValueError('Missing required parameters')
		if club_id not in self.__class__.votes:
			self.__class__.votes[club_id] = {}
		if book_id not in self.__class__.votes[club_id]:
			self.__class__.votes[club_id][book_id] = []
		self.__class__.votes[club_id][book_id].append(user_id)
