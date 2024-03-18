import json

def monitor_system():
    with open('urls.json', 'r') as file:
        data = json.load(file)
        return data