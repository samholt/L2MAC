from typing import Dict, List, Optional

# Mock database
users_db: Dict[str, Dict] = {}
posts_db: Dict[str, Dict] = {}
comments_db: Dict[str, Dict] = {}
likes_db: Dict[str, Dict] = {}
follows_db: Dict[str, Dict] = {}
messages_db: Dict[str, Dict] = {}
notifications_db: Dict[str, Dict] = {}
trends_db: Dict[str, Dict] = {}
interactions_db: Dict[str, Dict] = {}

# User schema
user_schema = ['email', 'username', 'password', 'profile_picture', 'bio', 'website_link', 'location', 'is_private']

# Post schema
post_schema = ['user_id', 'content', 'image', 'timestamp']

# Comment schema
comment_schema = ['user_id', 'post_id', 'content', 'timestamp']

# Like schema
like_schema = ['user_id', 'post_id', 'timestamp']

# Follow schema
follow_schema = ['follower_id', 'followee_id', 'timestamp']

# Message schema
message_schema = ['sender_id', 'receiver_id', 'content', 'timestamp']

# Notification schema
notification_schema = ['user_id', 'content', 'type', 'timestamp']

# Trend schema
trend_schema = ['hashtag', 'mentions']

# Interaction schema
interaction_schema = ['interaction_id', 'post_id', 'type']
