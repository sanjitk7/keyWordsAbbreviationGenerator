import re
def isMultiWordCamel(word):
    x = re.search(".*[a-z][A-Z].*",word)
    if (x):
    	print("Yes")
    else:
    	print("No")

def checkUnderscore(word):
    x = re.search("^[^_].*_.*[^_]$",word)
    if (x):
    	print("Yes")
    else:
    	print("No")

checkUnderscore("400_x_250_")