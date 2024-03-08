import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from views.user_view import UserView
from views.tweet_view import TweetView
from views.conversation_view import ConversationView
from views.trending_view import TrendingView

# Add your tests here
