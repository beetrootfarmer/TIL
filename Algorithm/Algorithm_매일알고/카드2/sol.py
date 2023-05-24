import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque(list(range(1,N+1)))

while len(q) > 1:
    q.popleft()
    b = q.popleft()
    q.append(b)
print(q[0])

