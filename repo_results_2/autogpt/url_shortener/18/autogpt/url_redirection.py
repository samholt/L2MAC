def redirect(short_url):
    # Read the URLs file
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    # Find the original URL that corresponds to the shortened URL
    for url in urls:
        if url['short_url'] == short_url:
            return url['original_url']
    # If the shortened URL is not found, return an error message
    return 'Error: Shortened URL not found'