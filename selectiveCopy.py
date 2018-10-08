import os, shutil, re


isPicture = re.compile(r'\w*.jpg$')

directory = input("Enter the absolute path that you would like to walk through: ")
for folderName, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        picture = isPicture.search(filename)
        if picture is not None:
            print('Found a .jpg in ' + folderName + ': ' + filename)
            print(os.path.abspath(filename))
            pictureAbsPath = os.path.abspath(filename)
            shutil.copy(os.path.abspath(filename), '/Users/corybasten/test')
            print(filename + ' was copied and moved to /Users/corybasten/test')
