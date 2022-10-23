from collections import deque
N = int(input())
dq = deque([i for i in range(1, N+1)])

while(len(dq) > 1):
    dq.popleft()
    mn = dq.popleft()
    dq.append(mn)
print(dq[0])

# 너 mu nu 무 king 받 음 
# 리스트는 시간초과 나고 같은 방식을 deque로 풀었을 때 시간초과가 안남
    