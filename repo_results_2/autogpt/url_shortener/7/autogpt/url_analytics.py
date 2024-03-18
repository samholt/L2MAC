def get_analytics(short_url):
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    return urls.get(short_url, {}).get('analytics', 'No analytics available')