# import os

# def presentdir(path):
#     items = os.listdir(path)
#     file_count = 0
#     for item in items:
#          os.path.isfile(os.path.join(path, item))
#          file_count += 1
    
#     return file_count

# path = "C:\\Users\\pc\\OneDrive\\Pictures"
# print(presentdir(path))
# print(os.listdir())



import os

def presentdir(path):
    file_count = len([item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))])
    directory_contents = os.listdir(path)
    return file_count, directory_contents

path = "C:\\Users\\pc\\OneDrive\\Documents"
file_count, directory_contents = presentdir(path)
print(f"Number of files: {file_count}")
print("Contents of the directory:", directory_contents)


