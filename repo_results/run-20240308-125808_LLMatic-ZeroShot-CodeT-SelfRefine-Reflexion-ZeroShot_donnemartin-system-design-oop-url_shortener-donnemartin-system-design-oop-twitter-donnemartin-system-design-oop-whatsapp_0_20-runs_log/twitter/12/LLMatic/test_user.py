import unittest
from user import User


class TestUser(unittest.TestCase):
	def setUp(self):
		self.users = [
			User(1, 'user1@example.com', 'user1', 'password1', 'profile_picture1', 'bio1', 'website_link1', 'location1'),
			User(2, 'user2@example.com', 'user2', 'password2', 'profile_picture2', 'bio2', 'website_link2', 'location2'),
			User(3, 'user3@example.com', 'user3', 'password3', 'profile_picture3', 'bio3', 'website_link3', 'location3'),
			User(4, 'user4@example.com', 'user4', 'password4', 'profile_picture4', 'bio4', 'website_link4', 'location4'),
			User(5, 'user5@example.com', 'user5', 'password5', 'profile_picture5', 'bio5', 'website_link5', 'location5')
		]
		self.users[0].follow(self.users[1])
		self.users[0].follow(self.users[2])
		self.users[1].follow(self.users[0])
		self.users[1].follow(self.users[2])
		self.users[2].follow(self.users[0])
		self.users[2].follow(self.users[1])
		self.users[3].follow(self.users[0])
		self.users[3].follow(self.users[1])
		self.users[4].follow(self.users[0])
		self.users[4].follow(self.users[1])

	def test_recommend_users(self):
		recommendations = self.users[0].recommend_users(self.users)
		self.assertEqual([user.id for user in recommendations], [2, 3])


if __name__ == '__main__':
	unittest.main()
