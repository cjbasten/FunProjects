import os


directory = input("Enter the absolute path that you would like to walk through: ")
for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        try:
            if os.path.getsize(filename) >= 1000:
                # Print the the absolute path and filename of files that are at least 1000 bytes.
                print(folderName + '/' + filename + ": " + str(os.path.getsize(filename)) + " bytes")
        except FileNotFoundError:
            continue
