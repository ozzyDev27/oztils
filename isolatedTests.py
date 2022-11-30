def x(n, b):
    if n==0:return 0
    digits = []
    while n:digits.append(int(n % b));n//=b
    return digits[::-1]
print(x(27,3))