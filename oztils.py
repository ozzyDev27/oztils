def nonIndexedRange(rangeInp): return list(range(1,int(rangeInp)+1))
def invert(arg):return eval(f"{str(type(arg))[8:-2]}(str(variableOfUnknownType)[::-1])")
def removeStart(start, strInp):return strInp[len(str(start)):] if strInp.startswith(str(start)) else strInp
def removeEnd(end, strInp):return strInp[:-len(str(end))] if strInp.endswith(str(end)) else strInp
def isPalindrome(check):return str(check)==str(check)[::-1]
def listToString(listInp):return [str(i) for i in listInp]
def listToInt(listInp):return [int(i) for i in listInp]
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
def percent(per):from random import randint;return randint(1,100)<=per
def coinFlip():from random import randint;return randint(0,1)<1
def formatNumber(n):return ",".join([str(round(n)-1 if round(n)>n else round(n))[::-1][i:i+3][::-1] for i in range(0, len(str(round(n)-1 if round(n)>n else round(n))), 3)][::-1])+"."+str(n).split(".",1)[1]
def reciprocal(n):return 1/n
def roundTo(n,roundTo):return round(n/roundTo)*roundTo
def clear():import os;os.system('cls' if os.name=='nt' else 'clear')
def pythagorean(a,b):return ((a**2)+(b**2))**.5
def pi():return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989
def slowprint(text, delay):
    from time import sleep
    for char in text:
        print(char, end="",flush=True)
        sleep(delay/len(text))
def remove(strIn, toRemove):
	for char in toRemove: strIn=strIn.replace(char,'')
	return strIn
def simplify(a,b):
	factsA=[]
	for checkA in range(1,round(a/2+1)):
		if a/checkA==round(a/checkA):factsA.append(checkA)
	facts=[]
	factsA.append(a)
	factsA=factsA[::-1]
	for _ in factsA:
		if b/_==round(b/_):facts.append(_);break
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
def getFactors(n):
	f=[1]
	for _ in range(2,round(n)+2 if round(n)>n else round(n)+1):f.append(_) if n%_==0 else (1+1)
	return f
def mustInput(s,w):
	n=input(s)
	while not n in w:n=input(s)
	return n
