import json

def get_all_urls():
    with open('urls.json', 'r') as file:
        return json.load(file)

def delete_url(url):
    with open('urls.json', 'r+') as file:
        urls = json.load(file)
        if url in urls:
            del urls[url]
            file.seek(0)
            json.dump(urls, file)
            return 'URL deleted successfully.'
        else:
            return 'Error: URL does not exist.'

def delete_user(username):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        if username in users:
            del users[username]
            file.seek(0)
            json.dump(users, file)
            return 'User deleted successfully.'
        else:
            return 'Error: User does not exist.'