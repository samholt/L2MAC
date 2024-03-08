class UserManager:
    def __init__(self):
        self.users = []

    def create_account(self, user):
        # Add user to list
        self.users.append(user)
        return 'Account created successfully'

    def manage_account(self, user_id, updated_user):
        # Find user by id
        for i, user in enumerate(self.users):
            if user['id'] == user_id:
                # Update user
                self.users[i] = updated_user
                return 'Account updated successfully'
        return 'Account not found'

    def save_favorite_recipe(self, user_id, recipe_id):
        # Find user by id
        for user in self.users:
            if user['id'] == user_id:
                # Add recipe to user's favorites
                user['favorites'].append(recipe_id)
                return 'Recipe added to favorites'
        return 'Account not found'

    def display_profile(self, user_id):
        # Find user by id
        for user in self.users:
            if user['id'] == user_id:
                # Return user's profile
                return user
        return 'Account not found'