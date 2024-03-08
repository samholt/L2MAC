class UserAccounts:
    def __init__(self):
        self.users = []

    def create_account(self, user):
        # Check if the user already exists
        if any(existing_user['username'] == user['username'] for existing_user in self.users):
            return False
        self.users.append(user)
        return True

    def manage_account(self, username, new_data):
        # Update user data
        for user in self.users:
            if user['username'] == username:
                user.update(new_data)
                return True
        return False

    def save_favorite_recipe(self, username, recipe_id):
        # Add the recipe to the user's list of favorite recipes
        for user in self.users:
            if user['username'] == username:
                user['favorite_recipes'].append(recipe_id)
                return True
        return False

    def display_profile(self, username):
        # Display the user's profile page
        for user in self.users:
            if user['username'] == username:
                return user
        return None