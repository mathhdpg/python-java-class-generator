import os

def write_to_file(folder, file_name, content):
    create_directory_if_not_exists(folder)
    with open(folder + file_name, "w") as file:
        file.write(content)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)