class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def view_all_urls(self):
        with open('url_database.txt', 'r') as file:
            return file.read()

    def delete_url(self, short_url):
        with open('url_database.txt', 'r') as file:
            lines = file.readlines()
        with open('url_database.txt', 'w') as file:
            for line in lines:
                if short_url not in line:
                    file.write(line)

    def delete_user(self, user):
        del user

    def view_analytics(self):
        with open('analytics.txt', 'r') as file:
            return file.read()