import unittest
import models


class TestModels(unittest.TestCase):
	def test_user(self):
		user = models.User(1, 'Test User', 'testuser@test.com', 'password', 'member')
		self.assertEqual(user.id, 1)
		self.assertEqual(user.username, 'Test User')
		self.assertEqual(user.email, 'testuser@test.com')
		self.assertEqual(user.password, 'password')
		self.assertEqual(user.role, 'member')

	def test_book_club(self):
		user1 = models.User(2, 'User1', 'user1@test.com', 'password', 'member')
		user2 = models.User(3, 'User2', 'user2@test.com', 'password', 'member')
		book_club = models.BookClub(1, 'Test Book Club', 'This is a test book club', 'public', [user1])
		self.assertEqual(book_club.id, 1)
		self.assertEqual(book_club.name, 'Test Book Club')
		self.assertEqual(book_club.description, 'This is a test book club')
		self.assertEqual(book_club.privacy, 'public')
		self.assertEqual(book_club.members, [user1])
		book_club.add_member(user2)
		self.assertEqual(book_club.members, [user1, user2])
		book_club.remove_member(user1)
		self.assertEqual(book_club.members, [user2])
		book_club.update_privacy('private')
		self.assertEqual(book_club.privacy, 'private')
		book_club.update_description('Updated description')
		self.assertEqual(book_club.description, 'Updated description')

	def test_meeting(self):
		meeting = models.Meeting(1, '2022-12-31', '12:00', 'Test Location', 'Test Agenda')
		self.assertEqual(meeting.id, 1)
		self.assertEqual(meeting.date, '2022-12-31')
		self.assertEqual(meeting.time, '12:00')
		self.assertEqual(meeting.location, 'Test Location')
		self.assertEqual(meeting.agenda, 'Test Agenda')

	def test_discussion(self):
		discussion = models.Discussion(1, 'Test Topic', ['Test Comment'], 0)
		self.assertEqual(discussion.id, 1)
		self.assertEqual(discussion.topic, 'Test Topic')
		self.assertEqual(discussion.comments, ['Test Comment'])
		self.assertEqual(discussion.votes, 0)


if __name__ == '__main__':
	unittest.main()
