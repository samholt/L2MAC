import unittest
from feed import Feed
from user import User

class TestFeed(unittest.TestCase):
	def setUp(self):
		self.user1 = User('user1', 'password1')
		self.user2 = User('user2', 'password2')
		self.user3 = User('user3', 'password3')
		self.user1.followed_users = [self.user2, self.user3]
		self.feed = Feed(self.user1)

	def test_generate_feed(self):
		# Assume that get_recent_activity method of User class returns the following data
		self.user2.get_recent_activity = lambda: [{'activity': 'posted a recipe', 'timestamp': '2022-01-01T00:00:00Z'}]
		self.user3.get_recent_activity = lambda: [{'activity': 'posted a review', 'timestamp': '2022-01-02T00:00:00Z'}]
		
		expected_feed = [
			{'activity': 'posted a review', 'timestamp': '2022-01-02T00:00:00Z'},
			{'activity': 'posted a recipe', 'timestamp': '2022-01-01T00:00:00Z'}
		]
		
		self.assertEqual(self.feed.generate_feed(), expected_feed)

if __name__ == '__main__':
	unittest.main()

