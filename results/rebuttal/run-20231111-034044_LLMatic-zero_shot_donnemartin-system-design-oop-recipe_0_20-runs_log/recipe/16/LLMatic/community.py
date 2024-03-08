class Community:
	def __init__(self):
		self.activity_log = []
		self.social_media_platforms = ['Facebook', 'Twitter', 'Instagram']

	def show_recent_activity(self, user):
		return [activity for activity in self.activity_log if activity['user'] == user]

	def share_on_social_media(self, recipe, platform):
		if platform not in self.social_media_platforms:
			return 'Invalid platform'
		else:
			return f'Sharing {recipe} on {platform}'
