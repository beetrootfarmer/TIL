#N을 소인수분해 하시오
N = int(input())
origin = N
g = 1 

if N ==1:
    print()
else:
    while(True):
        for i in range(2,N):
            if N%i ==0:
                N = N//i
                g = g * i
                print(i)
                break
            elif g*(i+1) == origin:
                g = g*(i+1)
                print(i+1)
                break
        if N == 1 or g == origin:
            break

#=========================위에꺼 시간초과=========================

import sys
N = int(sys.stdin.readline())
m = 2 
while N!=1: # N과m을 나눴을때 몫이 1이 되면 멈춤. 
    if N%m==0: 
        print(m) 
        N = N//m 
    else: m += 1
