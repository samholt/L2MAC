import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from models.tweet import Tweet
from models.direct_message import DirectMessage
from models.conversation import Conversation
from models.trending import Trending

# Add your tests here
