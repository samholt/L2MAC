from .file import File


class VersionedFile(File):
    def __init__(self, name, content, owner):
        super().__init__(name, content, owner)
        self.versions = [content]

    def update_content(self, new_content):
        super().update_content(new_content)
        self.versions.append(new_content)

    def get_version(self, version_number):
        if 0 <= version_number < len(self.versions):
            return self.versions[version_number]
        else:
            return None