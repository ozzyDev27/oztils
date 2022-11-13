def nonIndexedRange(rangeInp): return list(range(1,int(rangeInp)+1))
def invert(strInp):return str(strInp)[::-1]
def removeStart(start, strInp):
	if strInp.startswith(str(start)):return strInp[len(str(start)):]
	else:return strInp
def removeEnd(end, strInp):
	if strInp.endswith(str(end)):return strInp[:-len(str(end))]
	else:return strInp
def isPalindrome(check):return str(check)==str(check)[::-1]
def reverseList(ins):
	return list(ins)[::-1]
def listToString(listInp):return ''.join(listInp)
def slowprint(text: str, delay):
    from time import sleep
    for char in text:
        print(char, end="",flush=True)
        sleep(delay/len(text))
    print()
def remove(strIn, toRemove):
	for char in toRemove: strIn=strIn.replace(char,'')
	return strIn
def fileAppend(file,toWrite):
	localOpen = open(file, "a")
	localOpen.write(str(toWrite))
	localOpen.close()
def fileErase(file):
	localOpen = open(file, "w")
	localOpen.write("")
	localOpen.close()
def fileDelete(file):
	from os import remove
	remove(file)
def fileRename(file,toRename):
	from os import rename
	rename(file,toRename)
def isRound(num):return round(num)==num
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
	while target in ls:ls.pop(ls.index(target))
	return ls
def factorial(k):
	for i in range(k-1):k*=(k-i)
	return k
def bound(num,maxn,minn):sorted((minn, num, maxn))[1]
def getDifference(a,b):return abs(a-b)
def loop(value,minx,maxx):
	return ((value-minx)%(maxx-minx))+minx
def jumble(s):
	from random import shuffle
	l=s
	shuffle(l)
	return l
