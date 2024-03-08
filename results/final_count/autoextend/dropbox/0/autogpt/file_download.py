import os


class FileDownload:
    def __init__(self, user):
        self.user = user

    def download_file(self, file):
        # Retrieve file securely
        # Provide direct download link

    def download_folder_as_zip(self, folder):
        # Retrieve folder securely
        # Compress folder as ZIP
        # Provide direct download link


if __name__ == '__main__':
    # Retrieve user data securely
    user = None  # Replace with retrieved user data
    file_download = FileDownload(user)
    file = None  # Replace with file to be downloaded
    folder = None  # Replace with folder to be downloaded
    file_download.download_file(file)
    file_download.download_folder_as_zip(folder)
    print('File and folder download links provided.')