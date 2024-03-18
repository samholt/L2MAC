

def filter_posts(posts, criteria):
    return [post for post in posts if criteria(post)]


def search_posts(posts, keyword):
    return [post for post in posts if keyword in post.text]