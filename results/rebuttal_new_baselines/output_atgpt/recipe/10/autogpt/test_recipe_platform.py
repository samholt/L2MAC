import unittest
from recipe_platform import User, Recipe, Platform

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('testuser', 'testpassword')

    def test_register(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'testpassword')

    def test_login(self):
        self.assertEqual(self.user.login(), True)

    def test_submit_recipe(self):
        recipe = Recipe('testrecipe', ['ingredient1', 'ingredient2'], 'instructions')
        self.user.submit_recipe(recipe)
        self.assertEqual(self.user.recipes[0], recipe)

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe('testrecipe', ['ingredient1', 'ingredient2'], 'instructions')

    def test_rate(self):
        self.recipe.rate(5)
        self.assertEqual(self.recipe.ratings[0], 5)

    def test_review(self):
        self.recipe.review('Great recipe!')
        self.assertEqual(self.recipe.reviews[0], 'Great recipe!')

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = Platform()

    def test_register_user(self):
        user = User('testuser', 'testpassword')
        self.platform.register_user(user)
        self.assertEqual(self.platform.users[0], user)

    def test_login_user(self):
        user = User('testuser', 'testpassword')
        self.platform.register_user(user)
        self.assertEqual(self.platform.login_user('testuser', 'testpassword'), user)

    def test_submit_recipe(self):
        recipe = Recipe('testrecipe', ['ingredient1', 'ingredient2'], 'instructions')
        self.platform.submit_recipe(recipe)
        self.assertEqual(self.platform.recipes[0], recipe)

    def test_discover_recipe(self):
        recipe = Recipe('testrecipe', ['ingredient1', 'ingredient2'], 'instructions')
        self.platform.submit_recipe(recipe)
        self.assertEqual(self.platform.discover_recipe()[0], recipe)

if __name__ == '__main__':
    unittest.main()