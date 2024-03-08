class Discussion:
	def __init__(self):
		self.forums = {}

	def create_forum(self, forum_name):
		self.forums[forum_name] = {'comments': []}

	def post_comment(self, forum_name, comment):
		self.forums[forum_name]['comments'].append({'comment': comment, 'replies': []})

	def post_reply(self, forum_name, comment_index, reply):
		self.forums[forum_name]['comments'][comment_index]['replies'].append(reply)

	def upload_link(self, forum_name, link):
		self.forums[forum_name]['link'] = link

	def upload_image(self, forum_name, image):
		self.forums[forum_name]['image'] = image
