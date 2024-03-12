import unittest
from post import Post


class TestPost(unittest.TestCase):
	def setUp(self):
		self.posts = [
			Post(1, 1, 'Hello #world'),
			Post(2, 2, 'Good morning #world'),
			Post(3, 3, 'Good night #world'),
			Post(4, 4, 'Hello #python'),
			Post(5, 5, 'I love #python'),
			Post(6, 6, 'Hello #java'),
			Post(7, 7, 'I love #java'),
			Post(8, 8, 'Hello #javascript'),
			Post(9, 9, 'I love #javascript'),
			Post(10, 10, 'Hello #ruby')
		]

	def test_get_trending_hashtags(self):
		trending_hashtags = Post.get_trending_hashtags(self.posts)
		self.assertEqual(trending_hashtags, ['#world', '#python', '#java', '#javascript', '#ruby'])


if __name__ == '__main__':
	unittest.main()
