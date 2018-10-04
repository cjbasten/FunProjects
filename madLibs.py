import re

# Read a text file and save its contents as a string
madLibFile = open('madlib.txt')
readMadLib = madLibFile.read()
madLibFile.close()

# Open a new file and write the previous string to it.
newMadLibFile = open('madlibnew.txt', 'w')
newMadLibFile.write(readMadLib)
newMadLibFile.close()
newMadLibFile = open('madlibnew.txt')
readNewMadLibFile = newMadLibFile.read()
newMadLibFile.close()

# Regex to find the word to be substituted
adjToReplace = re.compile(r'ADJECTIVE')
nounToReplace = re.compile(r'NOUN')
verbToReplace = re.compile(r'VERB')
advToReplace = re.compile(r'ADVERB')

# Regex to verify if there are any more words to substitute
wordToReplace = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
# Loop through provided string and replace words one at a time
while wordToReplace.search(readNewMadLibFile) != None:
    if adjToReplace.search(readNewMadLibFile) != None:
        readNewMadLibFile = adjToReplace.sub(input("Enter an adjective:"), readNewMadLibFile, 1)
    if nounToReplace.search(readNewMadLibFile) != None:
        readNewMadLibFile = nounToReplace.sub(input("Enter a noun:"), readNewMadLibFile, 1)
    if verbToReplace.search(readNewMadLibFile) != None:
        readNewMadLibFile = verbToReplace.sub(input("Enter a verb:"), readNewMadLibFile, 1)
    if advToReplace.search(readNewMadLibFile) != None:
        readNewMadLibFile = advToReplace.sub(input("Enter an adverb:"), readNewMadLibFile, 1)

# Open the new file and overwrite it with the new string, including the answers to the Mad Lib
newMadLibFile = open('madlibnew.txt', 'w')
newMadLibFile.write(readNewMadLibFile)
newMadLibFile.close()
newMadLibFile = open('madlibnew.txt')
readNewMadLibFile = newMadLibFile.read()
newMadLibFile.close()
print(readNewMadLibFile)
