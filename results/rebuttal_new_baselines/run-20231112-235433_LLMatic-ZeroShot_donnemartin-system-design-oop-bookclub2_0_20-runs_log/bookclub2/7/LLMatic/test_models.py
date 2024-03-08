import unittest
import models

class TestModels(unittest.TestCase):
	def test_user(self):
		user = models.User(1, 'Test User', 'testuser@example.com', 'password')
		self.assertEqual(user.id, 1)
		self.assertEqual(user.username, 'Test User')
		self.assertEqual(user.email, 'testuser@example.com')
		self.assertEqual(user.password, 'password')

	def test_profile(self):
		profile = models.Profile(1, 'Bio', 'Location')
		self.assertEqual(profile.id, 1)
		self.assertEqual(profile.bio, 'Bio')
		self.assertEqual(profile.location, 'Location')

	def test_user_profile(self):
		user = models.User(1, 'Test User', 'testuser@example.com', 'password')
		profile = models.Profile(1, 'Bio', 'Location')
		user.set_profile(profile)
		self.assertEqual(user.profile, profile)

	def test_bookclub(self):
		bookclub = models.BookClub(1, 'Test BookClub', 'Description', 'Public')
		self.assertEqual(bookclub.id, 1)
		self.assertEqual(bookclub.name, 'Test BookClub')
		self.assertEqual(bookclub.description, 'Description')
		self.assertEqual(bookclub.privacy, 'Public')

	def test_meeting(self):
		bookclub = models.BookClub(1, 'Test BookClub', 'Description', 'Public')
		meeting = models.Meeting(1, '2022-01-01', '12:00', 'Location', bookclub)
		self.assertEqual(meeting.id, 1)
		self.assertEqual(meeting.date, '2022-01-01')
		self.assertEqual(meeting.time, '12:00')
		self.assertEqual(meeting.location, 'Location')
		self.assertEqual(meeting.bookclub, bookclub)

	def test_discussion(self):
		bookclub = models.BookClub(1, 'Test BookClub', 'Description', 'Public')
		discussion = models.Discussion(1, 'Test Discussion', 'Content', bookclub)
		self.assertEqual(discussion.id, 1)
		self.assertEqual(discussion.title, 'Test Discussion')
		self.assertEqual(discussion.content, 'Content')
		self.assertEqual(discussion.bookclub, bookclub)

	def test_comment(self):
		discussion = models.Discussion(1, 'Test Discussion', 'Content', None)
		comment = models.Comment(1, 'Test Comment', 1, discussion)
		self.assertEqual(comment.id, 1)
		self.assertEqual(comment.content, 'Test Comment')
		self.assertEqual(comment.user_id, 1)
		self.assertEqual(comment.discussion, discussion)

	def test_vote(self):
		bookclub = models.BookClub(1, 'Test BookClub', 'Description', 'Public')
		vote = models.Vote(1, 'Test Book', 1, bookclub)
		self.assertEqual(vote.id, 1)
		self.assertEqual(vote.book_name, 'Test Book')
		self.assertEqual(vote.user_id, 1)
		self.assertEqual(vote.bookclub, bookclub)

	def test_follow(self):
		user1 = models.User(1, 'Test User 1', 'testuser1@example.com', 'password')
		user2 = models.User(2, 'Test User 2', 'testuser2@example.com', 'password')
		user1.follow(user2)
		self.assertIn(user2, user1.following)
		self.assertIn(user1, user2.followers)

	def test_reading_list(self):
		user = models.User(1, 'Test User', 'testuser@example.com', 'password')
		book = 'Test Book'
		user.add_to_reading_list(book)
		self.assertIn(book, user.reading_list)

	def test_recommendation(self):
		user = models.User(1, 'Test User', 'testuser@example.com', 'password')
		book = 'Test Book'
		user.add_recommendation(book)
		self.assertIn(book, user.recommendations)

if __name__ == '__main__':
	unittest.main()

