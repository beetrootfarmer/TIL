#N을 소인수분해 하시오
N = int(input())
origin = N
g = 1 

if N ==1:
    print()
else:
    while(g != origin):
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
        if N == 1:
            break


