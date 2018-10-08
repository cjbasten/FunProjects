import os


directory = input("Enter the absolute path that you would like to walk through: ")
for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        if os.path.getsize(filename) >= 100:
            print(filename + ": " + str(os.path.getsize(filename)) + " bytes")
