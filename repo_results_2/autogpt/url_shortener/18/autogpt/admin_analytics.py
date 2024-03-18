def get_system_analytics():
    # Read the URLs file
    with open('urls.json', 'r') as file:
        urls = json.load(file)
    # Calculate the total number of URLs
    total_urls = len(urls)
    # Calculate the total number of clicks
    total_clicks = sum(url['clicks'] for url in urls)
    # Return the system performance and analytics
    return {'total_urls': total_urls, 'total_clicks': total_clicks}