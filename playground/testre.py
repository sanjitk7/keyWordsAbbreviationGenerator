import re
import timeit

start = timeit.default_timer()

def isMultiWordCamel(word):
    x = re.search(".*[a-z][A-Z].*",word)
    if (x):
        return True

def camelCaseSplit(str):
    if (str[0].islower()):
        camelCheck = re.findall(r'^[a-z]*|[A-Z]\w*',str)
        if  (isMultiWordCamel(camelCheck[1])):
            tempPascalSplit = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)
            tempPascalSplit.insert(0,camelCheck[0])
            return tempPascalSplit
    else:
        return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

splitWords = camelCaseSplit("DoCancelCallNow")
print("After Split:",splitWords)
stop = timeit.default_timer()
print("Time: ",stop-start)