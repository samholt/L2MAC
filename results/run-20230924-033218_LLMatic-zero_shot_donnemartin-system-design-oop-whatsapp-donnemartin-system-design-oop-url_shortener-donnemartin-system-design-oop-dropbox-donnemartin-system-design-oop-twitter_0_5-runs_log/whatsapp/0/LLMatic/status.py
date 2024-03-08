from datetime import datetime


class Status:
	def __init__(self, user, content, visibility='public'):
		self.user = user
		self.content = content
		self.timestamp = datetime.now()
		self.visibility = visibility
		self.viewers = []

	def post(self):
		return f'{self.user} posted: {self.content} at {self.timestamp}'

	def view(self, viewer):
		if self.visibility == 'public' or viewer in self.viewers:
			return self.content
		else:
			return 'This status is private.'

	def set_visibility(self, visibility):
		self.visibility = visibility

	def add_viewer(self, viewer):
		self.viewers.append(viewer)
