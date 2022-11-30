def getFactors(n):
	f=[1]
	for _ in range(2,round(n)+2 if round(n)>n else round(n)+1):f.append(_) if n%_==0 else (1+1)
	return f
print(getFactors(27))