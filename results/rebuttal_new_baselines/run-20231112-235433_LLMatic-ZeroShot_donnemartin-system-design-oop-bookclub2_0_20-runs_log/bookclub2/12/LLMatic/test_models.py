import unittest
from models import User, BookClub, Meeting, Discussion, Comment, Vote, Profile, Follow, ReadingList, Recommendation, Dashboard, Moderation, Analytics


class TestModels(unittest.TestCase):

	def test_user_model(self):
		user = User(username='test', email='test@test.com', password_hash='hashed_password')
		self.assertEqual(user.username, 'test')
		self.assertEqual(user.email, 'test@test.com')
		self.assertEqual(user.password_hash, 'hashed_password')

	def test_bookclub_model(self):
		bookclub = BookClub(name='test club')
		self.assertEqual(bookclub.name, 'test club')

	def test_meeting_model(self):
		meeting = Meeting(date='2022-01-01')
		self.assertEqual(meeting.date, '2022-01-01')

	def test_discussion_model(self):
		discussion = Discussion(topic='test topic')
		self.assertEqual(discussion.topic, 'test topic')

	def test_comment_model(self):
		comment = Comment(content='test content')
		self.assertEqual(comment.content, 'test content')

	def test_vote_model(self):
		vote = Vote(user_id=1, comment_id=1)
		self.assertEqual(vote.user_id, 1)
		self.assertEqual(vote.comment_id, 1)

	def test_profile_model(self):
		profile = Profile(user_id=1)
		self.assertEqual(profile.user_id, 1)

	def test_follow_model(self):
		follow = Follow(follower_id=1, followed_id=2)
		self.assertEqual(follow.follower_id, 1)
		self.assertEqual(follow.followed_id, 2)

	def test_readinglist_model(self):
		readinglist = ReadingList(user_id=1, book_id=1)
		self.assertEqual(readinglist.user_id, 1)
		self.assertEqual(readinglist.book_id, 1)

	def test_recommendation_model(self):
		recommendation = Recommendation(user_id=1, book_id=1)
		self.assertEqual(recommendation.user_id, 1)
		self.assertEqual(recommendation.book_id, 1)

	def test_dashboard_model(self):
		dashboard = Dashboard(user_id=1)
		self.assertEqual(dashboard.user_id, 1)

	def test_moderation_model(self):
		moderation = Moderation(user_id=1, comment_id=1)
		self.assertEqual(moderation.user_id, 1)
		self.assertEqual(moderation.comment_id, 1)

	def test_analytics_model(self):
		analytics = Analytics(user_id=1, bookclub_id=1)
		self.assertEqual(analytics.user_id, 1)
		self.assertEqual(analytics.bookclub_id, 1)


if __name__ == '__main__':
	unittest.main()
