import unittest
from user import User
from post import Post
from timeline import Timeline


class TestTimeline(unittest.TestCase):
	def setUp(self):
		self.user1 = User('user1@example.com', 'user1', 'password', False)
		self.user2 = User('user2@example.com', 'user2', 'password', False)
		self.user3 = User('user3@example.com', 'user3', 'password', False)
		self.post1 = Post(self.user1, 'Hello, world!')
		self.post2 = Post(self.user2, 'Hello, user1!')
		self.post3 = Post(self.user3, 'Hello, everyone!')
		self.user1.posts = [self.post1]
		self.user2.posts = [self.post2]
		self.user3.posts = [self.post3]
		self.user1.follow_user(self.user2)
		self.user1.follow_user(self.user3)
		self.timeline = Timeline(self.user1)

	def test_get_timeline_posts(self):
		timeline_posts = self.timeline.get_timeline_posts()
		self.assertIn(self.post2, timeline_posts)
		self.assertIn(self.post3, timeline_posts)


if __name__ == '__main__':
	unittest.main()
