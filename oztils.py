def nonIndexedRange(rangeInp): return list(range(1,int(rangeInp)+1))
def invert(strInp):return str(strInp)[::-1]
def removeStart(start, strInp):return strInp[len(str(start)):] if strInp.startswith(str(start)) else strInp
def removeEnd(end, strInp):return strInp[:-len(str(end))] if strInp.endswith(str(end)) else strInp
def isPalindrome(check):return str(check)==str(check)[::-1]
def reverseList(ins):return list(ins)[::-1]
def listToString(listInp):return ''.join(listInp)
def slowprint(text, delay):
    from time import sleep
    for char in text:
        print(char, end="",flush=True)
        sleep(delay/len(text))
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
def clamp(num,maxn,minn):sorted((minn, num, maxn))[1]
def getDifference(a,b):return abs(a-b)
def loop(value,minx,maxx):
	return ((value-minx)%(maxx-minx))+minx
def jumble(s):
	from random import shuffle
	shuffle(s)
	return s
def camelToUnder(camel):
	r=''
	for char in c:r+= f"_{char.lower()}" if char == char.upper() else char 
	return r
def stripNot(remove,string):
	r=''
	for char in string:r+=char if char in list(remove) else ''
	return r
def percent(per):
	from random import randint
	return True if randint(1,100)<=per else False
def coinFlip():
	from random import randint
	return True if randint(0,1)<1 else False
def query(q):
	from requests import get as g
	from bs4 import BeautifulSoup
	from cache_to_disk import cache_to_disk, NoCacheCondition
	@cache_to_disk(10)
	url = "https://www.google.com/search?q={}".format(q.replace(" ", "+"))
	response = g(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	open("output.html", "w").write(response.text)
	if answer := soup.find(class_='BNeawe iBp4i AP7Wnd'):res = (answer.text, True)
	elif snippet := soup.find(class_='BNeawe s3v9rd AP7Wnd'):
		[x.decompose() for x in snippet.find_all(name="a", recursive=True)]
		res = (snippet.text.replace(" · ", ''), False)
	return res[0]
def getFactors(n):
	f=[1]
	for _ in range(2,round((n/2))+3): 
		if n%_==0: f.append(_)
	f.append(n)
	return f
