import pytest
import random
import string

from recipe_platform import RecipeSubmission

def test_recipe_submission():
    # Generate random data for recipe submission
    title = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    ingredients = ['ingredient1', 'ingredient2']
    instructions = "Mix and cook"
    image = "image_url"

    submission = RecipeSubmission(title, ingredients, instructions, image)
    assert submission.is_valid()

def test_recipe_categorization():
    categories = ['Italian', 'Gluten-Free']
    submission = RecipeSubmission(title="Pizza", categories=categories)
    assert submission.has_valid_categories()

def test_recipe_edit_delete():
    recipe_id = random.randint(1, 1000)
    submission = RecipeSubmission.get_by_id(recipe_id)
    submission.edit(title="New Title")
    assert submission.title == "New Title"

    submission.delete()
    assert RecipeSubmission.get_by_id(recipe_id) is None

def test_recipe_format_validation():
    incomplete_data = {
        'title': '',
        'ingredients': []
    }
    submission = RecipeSubmission(**incomplete_data)
    assert not submission.is_valid()

def test_recipe_search():
    search_query = "chocolate"
    search_result = RecipeSubmission.search(search_query)
    assert all(search_query in recipe.title for recipe in search_result)

def test_recipe_categorization_search():
    category = 'Vegan'
    search_result = RecipeSubmission.search_by_category(category)
    assert all(category in recipe.categories for recipe in search_result)

def test_account_creation_management():
    user_data = {'username': 'user123', 'password': 'pass123'}
    user = User.create(**user_data)
    assert user.is_valid()

    user.change_password('newpass123')
    assert user.password == 'newpass123'

def test_save_favorite_recipes():
    user = User.get_by_username('user123')
    recipe_id = random.randint(1, 1000)
    user.save_favorite(recipe_id)
    assert recipe_id in user.favorites

def test_profile_page_content():
    user = User.get_by_username('user123')
    assert hasattr(user, 'submitted_recipes')
    assert hasattr(user, 'favorites')

def test_recipe_rating():
    recipe_id = random.randint(1, 1000)
    rating = random.randint(1, 5)
    RecipeRating.submit_rating(recipe_id, rating)
    assert RecipeRating.get_average_rating(recipe_id) >= 1

def test_recipe_review():
    recipe_id = random.randint(1, 1000)
    review = "Great recipe!"
    RecipeReview.submit_review(recipe_id, review)
    assert any(r.text == review for r in RecipeReview.get_reviews(recipe_id))

def test_display_average_rating():
    recipe_id = random.randint(1, 1000)
    average_rating = RecipeRating.get_average_rating(recipe_id)
    assert isinstance(average_rating, float) and 1 <= average_rating <= 5

def test_user_following():
    follower = User.get_by_username('user1')
    followee = User.get_by_username('chef1')
    follower.follow(followee.id)
    assert followee.id in follower.following

def test_feed_recent_activity():
    user = User.get_by_username('user1')
    feed = user.get_feed()
    assert 'recent_activity' in feed
    assert any(activity['type'] in ['new_recipe', 'new_rating'] for activity in feed['recent_activity'])

def test_recipe_sharing():
    recipe_id = random.randint(1, 1000)
    platforms = ['Facebook', 'Twitter', 'Instagram']
    for platform in platforms:
        assert RecipeSharing.share(recipe_id, platform) == True

def test_admin_manage_recipes():
    admin = Admin.get_by_username('admin1')
    recipe_id = random.randint(1, 1000)
    new_data = {'title': 'Updated Title'}
    admin.edit_recipe(recipe_id, new_data)
    recipe = RecipeSubmission.get_by_id(recipe_id)
    assert recipe.title == 'Updated Title'

def test_admin_remove_content():
    admin = Admin.get_by_username('admin1')
    inappropriate_recipe_id = random.randint(1, 1000)
    admin.remove_recipe(inappropriate_recipe_id)
    assert RecipeSubmission.get_by_id(inappropriate_recipe_id) is None

def test_admin_monitoring():
    admin = Admin.get_by_username('admin1')
    stats = admin.get_site_statistics()
    assert 'total_users' in stats and 'total_recipes' in stats

def test_recipe_recommendations():
    user = User.get_by_username('user1')
    recommendations = user.get_recommendations()
    assert len(recommendations) > 0

def test_new_recipe_notifications():
    user = User.get_by_username('user1')
    user.add_interest('Italian')
    notification = user.get_notifications()
    assert any('new_Italian_recipe' in n for n in notification)