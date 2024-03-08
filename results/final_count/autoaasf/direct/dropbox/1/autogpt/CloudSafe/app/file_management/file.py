import uuid


class File:
    def __init__(self, name, content, owner):
        self.id = uuid.uuid4()
        self.name = name
        self.content = content
        self.owner = owner

    def __str__(self):
        return f'File({self.name}, {self.owner})'

    def update_content(self, new_content):
        self.content = new_content

    def rename(self, new_name):
        self.name = new_name