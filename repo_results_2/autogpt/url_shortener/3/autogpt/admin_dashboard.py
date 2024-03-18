def view_all_urls():
    return read_file('urls.json')

def delete_url(short_url):
    urls = read_file('urls.json')
    for url, data in urls.items():
        if data['short'] == short_url:
            del urls[url]
            write_to_file('urls.json', urls)
            break

def delete_user(username):
    users = read_file('users.json')
    if username in users:
        del users[username]
        write_to_file('users.json', users)