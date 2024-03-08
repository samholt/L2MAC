def get_trending_topics():
    # Retrieve trending topics from database (to be implemented)
    trending_topics = []
    return trending_topics


def recommend_users(user_profile):
    # Retrieve users from database (to be implemented)
    all_users = []
    recommended_users = [user for user in all_users if user not in user_profile.following]
    return recommended_users
