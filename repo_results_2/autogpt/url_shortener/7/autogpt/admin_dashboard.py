def view_all_urls():
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    return urls