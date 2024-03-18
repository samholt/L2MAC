def redirect(short_url):
    with open('url_database.txt', 'r') as file:
        for line in file:
            original_url, shortened_url = line.split()
            if shortened_url == short_url:
                return original_url
    return 'Error: Shortened URL does not exist'