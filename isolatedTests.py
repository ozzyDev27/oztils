def removeAllOf(x,a):
  while x in a:a.pop(a.index(x))
  return a
