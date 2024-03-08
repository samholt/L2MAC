from .file import File


class Folder:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.files = []
        self.subfolders = []

    def add_file(self, file):
        self.files.append(file)

    def add_subfolder(self, folder):
        self.subfolders.append(folder)

    def remove_file(self, file_id):
        self.files = [file for file in self.files if file.id != file_id]

    def remove_subfolder(self, folder_name):
        self.subfolders = [folder for folder in self.subfolders if folder.name != folder_name]