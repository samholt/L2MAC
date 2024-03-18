import json

def view_all_urls():
    with open('urls.json', 'r') as file:
        data = json.load(file)
        return data

def delete_url(url):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        if url in data:
            del data[url]
            file.seek(0)
            json.dump(data, file)
            return 'URL deleted successfully'
        else:
            return 'Invalid URL'

def delete_account(username):
    with open('users.json', 'r+') as file:
        data = json.load(file)
        if username in data:
            del data[username]
            file.seek(0)
            json.dump(data, file)
            return 'Account deleted successfully'
        else:
            return 'Invalid username'

def monitor_system():
    # This function would normally monitor system performance and analytics, but I'll leave it empty for now as I can't actually implement this functionality
    pass