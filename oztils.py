import os

#range(3) returns [0,1,2], where nonIndexedRange(3) returns [1,2,3]
def nonIndexedRange(rangeInp):
	lst = list(range(int(rangeInp)))
	for i in lst: lst[i]+=1
	return lst

#If input "Hello", returns "olleH" - if input 125, return 521. If input ["world!", "Hello,"], return ["Hello,", "world!"]
def invert(strInp):
	return strInp[::-1]

#Removes version compatability - removeStart("Hello! ", "Hello! My name is Bill!") returns "My name is Bill!"
def removeStart(start, strInp):
	if strInp.startswith(str(start)):
		startLength=len(str(start))
		return strInp[startLength:]
	else:
		return strInp
def removeEnd(end, strInp):
	if strInp.endswith(str(end)):
		endLength=len(str(end))
		return strInp[:-endLength]
	else:
		return strInp	
#Checks if an input (string, int, list) is a palindrome
def isPalindrome(check):
	if check==check[::-1]: return True
	else: return False

#turns list into string
def listToString(listInp):
	return ''.join(listInp)

def cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    
    return wrapper

def ns_per_sec(num):
    return num * 10 ** 9 # 10 to the 9 is 1 billion

def replace_multiple(text, table):
    """replace using a dictionary
    Args:
        text ([string]): [text to be replaced]
        table ([dictionary]): [dictionary with keys as the target and values as what to replace targets with]
    """

    for key in table.keys():
        text = text.replace(key, table[key])

    return text

def slowprint(text, delay):
    from time import sleep
    for char in text:
        print(char, end="",flush=True)
        sleep(delay)
    print()

def remove(strIn, toRemove):
	for char in toRemove: strIn=strIn.replace(char,'')
	return strIn

def fileAppend(file,toWrite):
	localOpen = open(file, "a")
	localOpen.write(str(toWrite))
	localOpen.close()
def fileDestroy(file):
	localOpen = open(file, "w")
	localOpen.write("")
	localOpen.close()
def fileDelete(file):
	import os
	os.remove(file)
def fileRename(file,toRename):
	import os
	os.rename(file,toRename)
def last(listName):
	return listName[len(listName)-1]
