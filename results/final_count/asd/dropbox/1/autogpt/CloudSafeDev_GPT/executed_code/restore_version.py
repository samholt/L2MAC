import os
import shutil

# Function to restore a previous version of a file
def restore_version(filename, version):
    # Get base name and extension of file
    base, ext = os.path.splitext(filename)

    # Check if specified version exists
    if not os.path.exists(f'{base}_{version}{ext}'):
        return 'Specified version does not exist'

    # Replace current version with specified version
    shutil.copyfile(f'{base}_{version}{ext}', filename)

    # Return success message
    return f'Version {version} of file restored'

# Test function with dummy file and version
print(restore_version('test.txt', 1))