import os

folder_path = input("path to clean: ")

# Iterate over all the files in the folder
for file_name in os.listdir(folder_path):
    # Get the full path of the file
    file_path = os.path.join(folder_path, file_name)
    # Check if the file is an MP4 file
    if not file_name.endswith('.mp4'):
        # Delete the file
        os.remove(file_path)
