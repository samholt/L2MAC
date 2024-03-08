class UI:
	def __init__(self):
		self.theme = 'light'
		self.screen_size = 'medium'

	def switch_theme(self, theme):
		self.theme = theme
		return self.theme

	def adjust_screen_size(self, screen_size):
		self.screen_size = screen_size
		return self.screen_size

	def preview_file(self, file):
		return 'Preview of file: ' + file

