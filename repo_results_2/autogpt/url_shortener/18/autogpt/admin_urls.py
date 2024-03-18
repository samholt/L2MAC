def get_all_urls():
    # Read the URLs file
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    return urls