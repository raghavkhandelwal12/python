import os

def presentdir(path):
    file_count = len([item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))])
    directory_contents = os.listdir(path)
    return file_count, directory_contents

path = "C:\\Users\\pc\\OneDrive\\Documents"
file_count, directory_contents = presentdir(path)
print(f"Number of files: {file_count}")
print("Contents of the directory:", directory_contents)


