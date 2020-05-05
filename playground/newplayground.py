import re
import timeit

start = timeit.default_timer()

def isMultiWordCamel(word):
    x = re.search(".*[a-z][A-Z].*",word)
    if (x):
        return True

def camelCaseSplit(str):
    if (str[0].islower()):
        list1 =  re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)
        list2 =  re.findall(r'[a-z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)[0]
        res = []
        res.append(list2)
        for i in list1:
            res.append(i) 
        return res
    else:
        return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

splitWords = camelCaseSplit("doCancelCallNow")
print("After Split:",splitWords)
stop = timeit.default_timer()
print("Time: ",stop-start)


# import re 
  
# def camel_case_split(str): 
  
    # list1 =  re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str) 
    # list2 =  re.findall(r'[a-z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)[0];
    # res = []
    # res.append(list2)
    # for i in list1:
    #     res.append(i) 
    # return res
 
# str = "camelCaseString"
# print(camel_case_split(str))