def nonIndexedRange(rangeInp):
	lst = list(range(int(rangeInp)))
	for i in lst: lst[i]+=1
	return lst
def invert(strInp):return strInp[::-1]
def removeStart(start, strInp):
	if strInp.startswith(str(start)):
		startLength=len(str(start))
		return strInp[startLength:]
	else:return strInp
def removeEnd(end, strInp):
	if strInp.endswith(str(end)):
		endLength=len(str(end))
		return strInp[:-endLength]
	else:return strInp
def isPalindrome(check):
	if check==check[::-1]: return True
	else: return False
def listToString(listInp):return ''.join(listInp)
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
	import os
	localOpen = open(file, "a")
	localOpen.write(str(toWrite))
	localOpen.close()
def fileErase(file):
	import os
	localOpen = open(file, "w")
	localOpen.write("")
	localOpen.close()
def fileDelete(file):
	import os
	os.remove(file)
def fileRename(file,toRename):
	import os
	os.rename(file,toRename)
def isRound(num):
	if round(num)==num:return True
	else:return False
def intput(ina):
	try: return int(input(ina))
	except: return False
def simplify(a,b):
	factsA=[]
	for checkA in range(1,round(a/2+1)):
		if a/checkA==round(a/checkA):factsA.append(checkA)
	facts=[]
	factsA.append(a)
	factsA=factsA[::-1]
	for _ in factsA:
		if b/_==round(b/_):
			facts.append(_)
			break
	return [int(a/facts[len(facts)-1]),int(b/facts[len(facts)-1])]
def isPrime(n):
	for i in range(2,round(n/2)+2):
		if (n%i) == 0:return False
	return True
def deleteAllOf(ls,target):
	while target in ls:
		ls.pop(ls.index(target))
	return ls
def abs(n):
	if n<0: 
		try: return int(n*-1)
		except: return n*-1
	else: 
		try:return int(n)
		except: return n
def factorial(k):
	s=k
	for i in range(k-1):
		s-=1
		k*=s
	return k
def bound(num,maxn,minn):sorted((minn, num, maxn))[1]
