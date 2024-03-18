def delete_user(username):
    # Read the users file
    with open('users.json', 'r') as file:
        users = json.load(file)
    # Find the user that corresponds to the username
    for user in users:
        if user['username'] == username:
            # Remove the user from the list of users
            users.remove(user)
            # Write the updated users data back to the file
            with open('users.json', 'w') as file:
                json.dump(users, file)
            return 'User deleted successfully'
    # If the username is not found, return an error message
    return 'Error: User not found'