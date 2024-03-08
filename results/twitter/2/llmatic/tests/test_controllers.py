import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.user_controller import UserController
from controllers.tweet_controller import TweetController
from controllers.conversation_controller import ConversationController
from controllers.trending_controller import TrendingController

# Add your tests here
