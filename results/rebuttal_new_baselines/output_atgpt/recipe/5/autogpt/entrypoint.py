import os
import server
import recipe_management
import search_and_categorization
import user_accounts
import ratings_and_reviews

if __name__ == '__main__':
    server.setup()
    recipe_management.initialize()
    search_and_categorization.initialize()
    user_accounts.initialize()
    ratings_and_reviews.initialize()
    server.run()