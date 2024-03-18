def get_user_urls(username):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Find the user that corresponds to the username
    for user in users:
        if user['username'] == username:
            return user['urls']
    # If the username is not found, return an error message
    return 'Error: User not found'