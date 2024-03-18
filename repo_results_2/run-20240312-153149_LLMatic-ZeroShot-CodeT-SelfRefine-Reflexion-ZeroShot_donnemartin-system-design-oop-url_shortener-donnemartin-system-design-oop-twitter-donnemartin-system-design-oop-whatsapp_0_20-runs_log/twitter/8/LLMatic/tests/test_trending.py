import unittest
from trending import Trending

class TestTrending(unittest.TestCase):
	def setUp(self):
		self.trending = Trending()

	def test_add_hashtag(self):
		self.trending.add_hashtag('#test', 'USA')
		self.assertEqual(self.trending.hashtags, {'#test': 1})
		self.assertEqual(self.trending.locations, {'USA': {'#test': 1}})

	def test_get_trending_hashtags(self):
		self.trending.add_hashtag('#test', 'USA')
		self.trending.add_hashtag('#test2', 'USA')
		self.trending.add_hashtag('#test', 'USA')
		self.assertEqual(self.trending.get_trending_hashtags(), [('#test', 2), ('#test2', 1)])
		self.assertEqual(self.trending.get_trending_hashtags('USA'), [('#test', 2), ('#test2', 1)])

if __name__ == '__main__':
	unittest.main()

