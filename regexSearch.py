import re, os


# Return a list of filename strings for each file in the folder
files = os.listdir('/Users/corybasten/PycharmProjects/FunProjects')

# Have the user supply a regular expression to search
userSupplied = input('What would you like to search for?')
userRegEx = re.compile(userSupplied)

# Use a regular expression to find every string with a .txt at the end
isTextFile = re.compile(r'\w*.txt$')
for i in files:
    textFile = isTextFile.search(i)
    if textFile is not None:
        # print(textFile.group())
        openTextFile = open(i)
        readOpenTextFile = openTextFile.read()
        # print(readOpenTextFile)
        openTextFile.close()
        searchForText = userRegEx.findall(readOpenTextFile)
        # Print strings found by user supplied regular expression
        for foundText in searchForText:
            print('Match found: ' + foundText)
