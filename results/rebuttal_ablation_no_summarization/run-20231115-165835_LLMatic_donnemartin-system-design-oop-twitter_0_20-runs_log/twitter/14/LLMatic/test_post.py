import unittest
from post import Post
from user import User

class TestPost(unittest.TestCase):
	def setUp(self):
		self.user = User('test@test.com', 'testuser', 'testpass')
		self.post = Post(self.user, 'Hello, world! #greeting')

	def test_edit_post(self):
		self.post.edit_post('Hello, universe! #greeting')
		self.assertEqual(self.post.text, 'Hello, universe! #greeting')

	def test_delete_post(self):
		self.post.delete_post()
		self.assertIsNone(self.post.text)
		self.assertIsNone(self.post.user)
		self.assertEqual(self.post.images, [])

	def test_like_post(self):
		self.post.like_post()
		self.assertEqual(self.post.likes, 1)

	def test_retweet_post(self):
		self.post.retweet_post()
		self.assertEqual(self.post.retweets, 1)

	def test_reply_to_post(self):
		reply = Post(self.user, 'Nice post!')
		self.post.reply_to_post(self.user, 'Nice post!')
		self.assertEqual(self.post.replies[0].text, reply.text)
		self.assertEqual(self.post.replies[0].user, reply.user)

	def test_get_trending_topics(self):
		posts = [Post(self.user, 'Hello, world! #greeting'), Post(self.user, 'Goodbye, world! #farewell'), Post(self.user, 'Hello again, world! #greeting'), Post(self.user, 'Hello again, world! #greeting')]
		trending_topics = Post.get_trending_topics(posts)
		self.assertEqual(trending_topics, ['#greeting'])

if __name__ == '__main__':
	unittest.main()
