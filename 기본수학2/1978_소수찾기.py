N = int(input())
num = list(map(int,input().split()))
s = N
for i in range(0,N):
    m = num[i] #num[0]=1 3 5 7
    if m == 1 :
        s -= 1
    else:
        for n in range(2,m):
            if m % n == 0:
                s -= 1
                break
print(s)