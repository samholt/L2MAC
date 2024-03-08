import pytest
from recipe import Recipe


def test_share_on_social_media():
	recipe = Recipe(['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', 'category', 'dietary_needs', '2022-01-01')
	assert recipe.share_on_social_media() == 'Shared on social media'
