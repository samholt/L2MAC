import os
import shutil

# Function to create a new version of a file
def version_file(filename):
    # Get base name and extension of file
    base, ext = os.path.splitext(filename)

    # Get list of existing versions
    versions = [f for f in os.listdir('.') if f.startswith(base) and f != filename]

    # Get new version number
    version = max([int(v.split('_')[-1]) for v in versions] or [0]) + 1

    # Create new version of file
    shutil.copyfile(filename, f'{base}_{version}{ext}')

    # Return success message
    return f'New version of file created: {base}_{version}{ext}'

# Test function with dummy file
print(version_file('test.txt'))