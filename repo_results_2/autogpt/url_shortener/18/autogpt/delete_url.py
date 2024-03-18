def delete_url(username, short_url):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Find the user that corresponds to the username
    for user in users:
        if user['username'] == username:
            # Find the URL that corresponds to the shortened URL
            for url in user['urls']:
                if url['short_url'] == short_url:
                    # Remove the URL from the user's list of URLs
                    user['urls'].remove(url)
                    # Write the updated users data back to the file
                    with open('users.json', 'w') as file:
                        json.dump(users, file)
                    return 'URL deleted successfully'
    # If the username or the shortened URL is not found, return an error message
    return 'Error: User or URL not found'