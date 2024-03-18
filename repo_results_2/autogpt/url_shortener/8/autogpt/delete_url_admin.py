import json

def delete_url_admin(short_url):
    with open('urls.json', 'r+') as file:
        data = json.load(file)
        if short_url in data:
            del data[short_url]
            file.seek(0)
            json.dump(data, file)
        else:
            return 'This short URL does not exist.'