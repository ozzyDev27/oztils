def nonIndexedRange(rangeInp): return list(range(1,int(rangeInp)+1))
def invert(strInp):return str(strInp)[::-1]
def removeStart(start, strInp):return strInp[len(str(start)):] if strInp.startswith(str(start)) else strInp
def removeEnd(end, strInp):return strInp[:-len(str(end))] if strInp.endswith(str(end)) else strInp
def isPalindrome(check):return str(check)==str(check)[::-1]
def listToString(listInp):return ''.join(listInp)
def isRound(num):return round(num)==num
def factorial(n):return n * factorial(n-1) if n else 1
def clamp(num,maxn,minn):sorted((minn, num, maxn))[1]
def getDifference(a,b):return abs(a-b)
def loop(value,minx,maxx):return ((value-minx)%(maxx-minx))+minx
def jumble(s):from random import shuffle;shuffle(s);return s
def fileDelete(file):from os import remove;remove(file)
def fileRename(file,toRename):from os import rename;rename(file,toRename)
def fileAppend(file,toWrite):localOpen = open(file, "a");localOpen.write(str(toWrite));localOpen.close()
def fileErase(file):localOpen = open(file, "w");localOpen.write("");localOpen.close()
def isUnique(l):return sorted(list(dict.fromkeys(l)))==sorted(l)
def mean(numbers):return sum(numbers)/len(numbers)
def sqrt(n):return n**.5
def num(n):return int(n) if float(n).endswith(".0") else float(n)
def xor(a,b):return (a or b) and (not a and b)
def ceil(n):return round(n)+1 if round(n)<n else round(n)
def floor(n):return round(n)+1 if round(n)>n else round(n)
def isPrime(n):return 0 not in [n%i for i in range(2,n//2+1)]
def slowprint(text, delay):
    from time import sleep
    for char in text:
        print(char, end="",flush=True)
        sleep(delay/len(text))
def remove(strIn, toRemove):
	for char in toRemove: strIn=strIn.replace(char,'')
	return strIn
def intput(ina):
	try: return int(input(ina))
	except: pass
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
def deleteAllOf(ls,target):
	while target in ls:ls.pop(ls.index(target))
	return ls
def camelToUnder(camel):
	r=''
	for char in camel:r+= f"_{char.lower()}" if char == char.upper() else char 
	return r
def stripNot(remove,string):
	r=''
	for char in string:r+=char if char in list(remove) else ''
	return r
def percent(per):
	from random import randint
	return randint(1,100)<=per
def coinFlip():
	from random import randint
	return randint(0,1)<1
def getFactors(n):
	f=[1]
	for _ in range(2,round(n)+2 if round(n)>n else round(n)+1): 
		if n%_==0: f.append(_)
	f.append(n)
	return f
def mustInput(s,w):
	n=input(s)
	while not n in w:n=input(s)
