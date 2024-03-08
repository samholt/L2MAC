import heapq


def get_trending_topics(posts, top_n=10):
    hashtag_count = {}
    for post in posts:
        hashtags = set(re.findall(r'#\w+', post.content))
        for hashtag in hashtags:
            if hashtag in hashtag_count:
                hashtag_count[hashtag] += 1
            else:
                hashtag_count[hashtag] = 1

    top_hashtags = heapq.nlargest(top_n, hashtag_count, key=hashtag_count.get)
    return top_hashtags


def recommend_users_to_follow(user, users, mutual_followers_threshold=3):
    # TODO: Retrieve user relationships from database
    user_relationships = []

    mutual_followers_count = {}
    for relationship in user_relationships:
        if relationship.follower == user:
            continue
        mutual_followers = set(relationship.follower.followers).intersection(user.followers)
        if len(mutual_followers) >= mutual_followers_threshold:
            mutual_followers_count[relationship.follower] = len(mutual_followers)

    recommended_users = heapq.nlargest(10, mutual_followers_count, key=mutual_followers_count.get)
    return recommended_users
