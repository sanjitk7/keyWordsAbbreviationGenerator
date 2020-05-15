# Chithappa's tweaked script - Incorporated modifications: ignote _ words, accept camelCase and PascalCase. Test Cases run.

import re
import json

#check camel case 2 words
def isMultiWordCamel(word):
    # x = re.search(".*[a-z].*",word)
    x = re.search(r"(.+?)([A-H])",word)
    if (x):
        return True
    return False

#check _ words
def checkUnderscore(word):
    # x = re.search("^[^_].*_.*[^_]$",word)
    x = re.search(r"(.*?)_([a-zA-Z])",word)
    if (x):
        return True

#split camel case words
def camelCaseSplit(str):
    if (str[0].islower()):
        camelCheck = re.findall(r'^[a-z]*|[A-Z]\w*',str)
        if  (isMultiWordCamel(camelCheck[1])):
            tempPascalSplit = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)
            tempPascalSplit.insert(0,camelCheck[0])
            return tempPascalSplit
    else:
        return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)


#adding keywords to respective acronym
def addToDict(acronym,keyword):
    if (acronym in abbrDict):
        abbrDict[acronym].append(keyword)
    else:
        abbrDict[acronym] = [keyword]

def main(word):
    if ((not word == "" and not checkUnderscore(word)) and (not word.isupper()) and isMultiWordCamel(word)):
        if('_' in word):
            SplitWords = word.split('_')
        elif (isMultiWordCamel(word)):
            SplitWords = camelCaseSplit(word)

        tempAcronym = ""
        # print("splitwords:", SplitWords)
        for w in SplitWords:
            tempAcronym += w[0]
        return tempAcronym.lower()
    else:
        return ""


if (__name__=="__main__"):
    file_in_path = "/Users/sanjitkumar/personal_projects/keyWordsAcronymGenerator/words.txt"
    file_op_path = "/Users/sanjitkumar/personal_projects/keyWordsAcronymGenerator/output.json"
    #dictionary for words
    abbrDict = {}

    with open(file_in_path) as f:
        fileWords = f.readlines()

    for word in fileWords:
        word = word.strip('\n').strip()
        abbreviation = main(word)

        if (abbreviation!="" and (len(abbreviation) > 1)):
            addToDict(abbreviation,word)

    #print("abbreviation: ",abbrDict)
    json = json.dumps(abbrDict)
    with open(file_op_path, "w") as fout:
        fout.write(json)


    # Iterate over items in dict and print line by line
    # summaryDict = {}
    # for key, value in abbrDict.items():
    #         summaryDict[key] = len(value)

    # sortedKeyBased = {key:value for key, value in sorted(summaryDict.items(), key=lambda k: (len(k[0]),k[0],k[1]),reverse = True)} 
    # [print(k,v) for k,v in sortedKeyBased.items()]

    # print("============================")
            
    # sortedSummary = { key: value for key, value in sorted(summaryDict.items(), key=lambda item: item[0],reverse = True)}
    # [print(k,v) for k,v in sortedSummary.items()]
    # print(abbrDict)