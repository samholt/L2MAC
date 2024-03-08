import unittest
from recommendation import Recommendation
from user import User
from recipe import Recipe

class TestRecommendation(unittest.TestCase):
	def setUp(self):
		self.users = {'John': User('John', 'password1'), 'Jane': User('Jane', 'password2')}
		self.users['John'].favorite_recipes = ['Italian', 'Mexican']
		self.users['Jane'].favorite_recipes = ['Chinese']
		self.recipes = [Recipe(1, 'Pizza', 'Italian', ['ingredient1', 'ingredient2'], 'instructions', [], []), Recipe(2, 'Tacos', 'Mexican', ['ingredient1', 'ingredient2'], 'instructions', [], []), Recipe(3, 'Fried Rice', 'Chinese', ['ingredient1', 'ingredient2'], 'instructions', [], [])]
		self.recommendation = Recommendation(self.users, self.recipes)

	def test_generate_recommendations(self):
		# Test for user 'John'
		recommended_recipes = self.recommendation.generate_recommendations('John')
		self.assertEqual(recommended_recipes, [self.recipes[0], self.recipes[1]])

	def test_notify_user(self):
		# Test for user 'John'
		self.recommendation.notify_user('John')
		self.assertEqual(self.users['John'].notifications, [self.recipes[0], self.recipes[1]])

if __name__ == '__main__':
	unittest.main()
