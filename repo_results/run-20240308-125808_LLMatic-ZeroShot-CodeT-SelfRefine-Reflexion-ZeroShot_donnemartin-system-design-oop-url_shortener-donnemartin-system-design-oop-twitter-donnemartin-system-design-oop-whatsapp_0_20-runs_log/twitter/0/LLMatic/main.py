from user_management import UserManagement
from posting_content_management import PostingContentManagement
from social_interaction import SocialInteraction
from trending_discovery import TrendingDiscovery

class OnlineMicrobloggingService:
	def __init__(self):
		self.user_management = UserManagement()
		self.posting_content_management = PostingContentManagement()
		self.social_interaction = SocialInteraction()
		self.trending_discovery = TrendingDiscovery()
