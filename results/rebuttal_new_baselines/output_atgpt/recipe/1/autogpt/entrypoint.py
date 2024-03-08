import os
import server
import recipe_management
import search_and_categorization
import user_accounts
import ratings_and_reviews

if __name__ == '__main__':
    server.setup()
    server.run()