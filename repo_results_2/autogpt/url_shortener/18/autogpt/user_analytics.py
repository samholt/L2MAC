def get_user_analytics(username):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Find the user that corresponds to the username
    for user in users:
        if user['username'] == username:
            # Get the analytics for all the user's URLs
            analytics = [get_url_statistics(url['short_url']) for url in user['urls']]
            return analytics
    # If the username is not found, return an error message
    return 'Error: User not found'