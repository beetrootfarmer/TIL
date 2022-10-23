from collections import deque


N = int(input())
deque = deque([i for i in range(2, N+1)])

if N % 2:
    deque.append(deque.popleft())
while(len(deque) > 1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
print(deque[0])

# 너 mu nu 무 king 받 음 
# 리스트는 시간초과 나고 같은 방식을 deque로 풀었을 때 시간초과가 안남
    