from dataclasses import dataclass, field

@dataclass
class Comment:
	author: str
	content: str
	parent_post: str
	likes: int = field(default=0)

	def like(self):
		self.likes += 1

	def delete(self):
		self.content = ''
		self.likes = 0
