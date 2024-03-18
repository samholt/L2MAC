def set_expiration(username, short_url, expiration):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Find the user that corresponds to the username
    for user in users:
        if user['username'] == username:
            # Find the URL that corresponds to the shortened URL
            for url in user['urls']:
                if url['short_url'] == short_url:
                    # Set the expiration date/time
                    url['expiration'] = expiration
                    # Write the updated users data back to the file
                    with open('users.json', 'w') as file:
                        json.dump(users, file)
                    return 'Expiration set successfully'
    # If the username or the shortened URL is not found, return an error message
    return 'Error: User or URL not found'