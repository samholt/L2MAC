def delete_url(short_url):
    # Read the URLs file
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    # Find the URL that corresponds to the shortened URL
    for url in urls:
        if url['short_url'] == short_url:
            # Remove the URL from the list of URLs
            urls.remove(url)
            # Write the updated URLs data back to the file
            with open('urls.json', 'w') as file:
                json.dump(urls, file)
            return 'URL deleted successfully'
    # If the shortened URL is not found, return an error message
    return 'Error: URL not found'