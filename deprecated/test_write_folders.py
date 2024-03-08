import os
# from examples.parking_current_state import file_dict
from examples.parking_round_one import file_dict
from summarizer_and_modifier import remove_line_numbers, fix_line_spacings
import json

def write_files_from_dict(file_dict, base_dir="output"):
    """
    Writes files to a folder based on the given dictionary.
    
    :param file_dict: Dictionary with filenames as keys and lists of file content as values.
    :param base_dir: Base directory where files should be saved.
    """
    # Ensure base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Iterate through the file dictionary
    for file_path, lines in file_dict.items():
        # Construct the full path for the file
        full_path = os.path.join(base_dir, file_path)
        
        # Create the directories if they don't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        lines = fix_line_spacings(remove_line_numbers(lines))
        # Write content to the file
        with open(full_path, "w") as f:
            for line in lines:
                f.write(line + "\n")

# data = json.loads(data)
# file_dict = data['file_dict']
write_files_from_dict(file_dict)