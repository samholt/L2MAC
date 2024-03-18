def edit_url(username, old_short_url, new_short_url):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Find the user that corresponds to the username
    for user in users:
        if user['username'] == username:
            # Find the URL that corresponds to the old shortened URL
            for url in user['urls']:
                if url['short_url'] == old_short_url:
                    # Update the shortened URL
                    url['short_url'] = new_short_url
                    # Write the updated users data back to the file
                    with open('users.json', 'w') as file:
                        json.dump(users, file)
                    return 'URL edited successfully'
    # If the username or the old shortened URL is not found, return an error message
    return 'Error: User or URL not found'