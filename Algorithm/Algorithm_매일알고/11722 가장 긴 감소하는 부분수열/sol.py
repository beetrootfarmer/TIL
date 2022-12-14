import sys
N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

dp = [1] * N                                # 값을 비교해서 카운팅한 것을 저장할 리스트

for i in range(1, N):                       # 전체 수열의 길이만큼 순회
    for j in range(i):                      # 해당 수의 앞에 위치한 수를 탐색해서
        if data[i] < data[j]:               # 해당 수보다 값이 크면
            dp[i] = max(dp[j] + 1, dp[i])   # 해당 수 위의 값이 카운팅한것 +1 혹은 해당 수의 카운팅 중 더 큰 값을 저장

print(max(dp))