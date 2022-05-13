def hano(n, x, y):
    if n == 1:
        print(x, y)
        return
    
    if n > 1:
        hano(n - 1, x, 6 - x - y)
    
    print (x, y)

    if n > 1:
        hano(n - 1, 6 - x - y, y)

n = int(input())
print(2**n-1)
hano(n, 1, 3)