import os

def presentdir(path):
    items = os.listdir(path)
    file_count = 0
    for item in items:
         os.path.isfile(os.path.join(path, item))
         file_count += 1
    
    return file_count

path = 'c:\\Users\\pc\\OneDrive\\Documents\\raghav.py'
print(presentdir(path))
print(os.listdir())