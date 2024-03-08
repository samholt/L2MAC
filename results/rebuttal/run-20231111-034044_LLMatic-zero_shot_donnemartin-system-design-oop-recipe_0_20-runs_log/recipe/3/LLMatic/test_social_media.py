from social_media import SocialMedia

def test_social_media():
	# Initialize SocialMedia class
	social_media = SocialMedia()

	# Test sharing on Facebook
	assert social_media.share_on_facebook('Recipe 1') == 'Shared Recipe 1 on Facebook'

	# Test sharing on Twitter
	assert social_media.share_on_twitter('Recipe 1') == 'Shared Recipe 1 on Twitter'

	# Test sharing on Instagram
	assert social_media.share_on_instagram('Recipe 1') == 'Shared Recipe 1 on Instagram'
