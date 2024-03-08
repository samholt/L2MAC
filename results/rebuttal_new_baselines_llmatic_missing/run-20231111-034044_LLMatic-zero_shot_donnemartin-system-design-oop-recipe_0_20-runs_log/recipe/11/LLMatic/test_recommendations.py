from recommendations import RecommendationManager
from users import UserManager, User
from recipes import RecipeManager
from database import MockDatabase

def test_get_recommendations():
	db = MockDatabase()
	user_manager = UserManager(db)
	recipe_manager = RecipeManager(db)
	recommendation_manager = RecommendationManager(db)

	# Create users
	user1 = user_manager.create_user(1, 'User 1', 'user1@example.com')
	user2 = user_manager.create_user(2, 'User 2', 'user2@example.com')
	user3 = user_manager.create_user(3, 'User 3', 'user3@example.com')

	# User 1 follows User 2 and User 3
	user1.follow(user2)
	user1.follow(user3)

	# User 2 and User 3 submit recipes
	recipe1 = recipe_manager.submit_recipe(1, 2, 'Recipe 1', 'Description 1', 'Ingredients 1', 'Category 1')
	recipe2 = recipe_manager.submit_recipe(2, 3, 'Recipe 2', 'Description 2', 'Ingredients 2', 'Category 1')
	recipe3 = recipe_manager.submit_recipe(3, 2, 'Recipe 3', 'Description 3', 'Ingredients 3', 'Category 2')
	recipe4 = recipe_manager.submit_recipe(4, 3, 'Recipe 4', 'Description 4', 'Ingredients 4', 'Category 2')

	# Add users and recipes to the database
	db.add_user(user1)
	db.add_user(user2)
	db.add_user(user3)
	db.add_recipe(recipe1)
	db.add_recipe(recipe2)
	db.add_recipe(recipe3)
	db.add_recipe(recipe4)

	# Get recommendations for User 1
	recommendations = recommendation_manager.get_recommendations(1)

	# Check that the recommendations are correct
	assert len(recommendations) == 2
	assert all(recipe['category'] == 'Category 1' for recipe in recommendations)
	assert all(recipe['user_id'] in [user2.id, user3.id] for recipe in recommendations)
