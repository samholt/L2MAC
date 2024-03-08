class Forum:
	def __init__(self, book_club):
		self.book_club = book_club
		self.threads = []

	def create_thread(self, title, author):
		thread = {'title': title, 'author': author, 'comments': []}
		self.threads.append(thread)
		return thread

	def add_comment(self, thread_title, comment, author):
		for thread in self.threads:
			if thread['title'] == thread_title:
				thread['comments'].append({'comment': comment, 'author': author})
				return thread
		return None
