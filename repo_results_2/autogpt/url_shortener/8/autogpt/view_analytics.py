import json

def view_analytics(username):
    with open('users.json', 'r') as file:
        user_data = json.load(file)
        if username in user_data:
            urls = user_data[username]['urls']
            with open('urls.json', 'r') as url_file:
                url_data = json.load(url_file)
                analytics = {url: url_data[url] for url in urls if url in url_data}
                return analytics
        else:
            return 'This username does not exist.'