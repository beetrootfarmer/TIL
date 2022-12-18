import sys
N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

dp = [1] * N                                

for i in range(1, N):                       
    for j in range(i):
                       
        if data[i] > data[j]:    
            print('i =', i, ', j=', j)                  
            dp[i] = max(dp[j] + 1, dp[i])   

print(max(dp))