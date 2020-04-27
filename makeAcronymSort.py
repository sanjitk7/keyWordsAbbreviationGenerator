import re

file_path = "words.txt"
#dictionary for words
acryDict = {}

with open(file_path) as f:
    fileWords = f.readlines()

#check camel case 2 words
def isMultiWordCamel(word):
    x = re.search(".*[a-z][A-Z].*",word)
    if (x):
        return True

#check _ words
def checkUnderscore(word):
    x = re.search("^[^_].*_.*[^_]$",word)
    if (x):
        return True

#split camel case words
def camelCaseSplit(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

#adding keywords to respective acronym
def addToDict(acronym,keyword):
    if (acronym in acryDict):
        acryDict[acronym].append(keyword)
    else:
        acryDict[acronym] = [keyword]

def main(word):
    if ((not word == "") and (not word.isupper()) and (checkUnderscore(word)
 or isMultiWordCamel(word))):
        if('_' in word):
            SplitWords = word.split('_')
        elif (isMultiWordCamel(word)):
            SplitWords = camelCaseSplit(word)


        tempAcronym = ""
        for w in SplitWords:
            #print("w:", w)
            tempAcronym += w[0]
        return tempAcronym.lower()
    else:
        return ""

# #screen and ignore single words and caps words
# print("List of all words from the file:\n")

for word in fileWords:
    word = word.strip('\n').strip()
    result = main(word)


    if (result!=""):
        addToDict(result,word)

print(acryDict)