import re


def search_posts(posts, query):
    query = query.lower()
    results = []
    for post in posts:
        if query in post.content.lower():
            results.append(post)
    return results


def filter_posts(posts, filter_type, filter_value):
    if filter_type == 'hashtag':
        pattern = re.compile(r'#\w+')
    elif filter_type == 'mention':
        pattern = re.compile(r'@\w+')
    else:
        raise ValueError('Invalid filter type.')

    results = []
    for post in posts:
        if pattern.search(post.content):
            results.append(post)
    return results


def search_users(users, query):
    query = query.lower()
    results = []
    for user in users:
        if query in user.username.lower() or query in user.email.lower():
            results.append(user)
    return results
