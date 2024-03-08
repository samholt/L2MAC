import pytest
from recipe_platform.database import get_user_by_username, get_admin_by_username, get_recipe_by_id, get_recipe_ratings_by_id, get_recipe_reviews_by_id, get_recipe_shares_by_id


def test_get_user_by_username():
	user = get_user_by_username('user1')
	assert user is not None


def test_get_admin_by_username():
	admin = get_admin_by_username('admin1')
	assert admin is not None


def test_get_recipe_by_id():
	recipe = get_recipe_by_id(1)
	assert recipe is not None


def test_get_recipe_ratings_by_id():
	ratings = get_recipe_ratings_by_id(1)
	assert ratings is not None


def test_get_recipe_reviews_by_id():
	reviews = get_recipe_reviews_by_id(1)
	assert reviews is not None


def test_get_recipe_shares_by_id():
	shares = get_recipe_shares_by_id(1)
	assert shares is not None
