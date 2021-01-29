import os

file_path = input()

if not os.path.exists(file_path):
    print("File already deleted!")

else:
    os.remove(file_path)
    print("Deleted!")
