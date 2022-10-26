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
