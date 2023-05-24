import sys
from collections import deque
input = sys.stdin.readline

n, T = map(int, input().rstrip().split())
holds = set()
for i in range(n):
    holds.add(tuple(map(int, input().rstrip().split())))

dq = deque()
dq.append([0,0,0])
step = []
visited = [0] * n

def move(x,y,s):
    if y > T:
        return
    if y == T:
        step.append(s)
        return
    for i,(xx,yy) in enumerate(holds):
        if abs(x-xx) <=2 and abs(y-yy) <=2 and not visited[i]:
            visited[i] = 1
            move(xx, yy, s+1)

# move(0,0,0)


## 런타임에러가 난다 . 왜지?
## deque를 사용하는 식으로 다시 풀기

while dq:
    x, y,s = dq.popleft()
    if y == T:
        step.append(s)
        # break
    for xm in range(-2,3):
        for ym in range(-2,3):
            xx, yy = xm+x, ym+y
            if (xx, yy) in holds:
                dq.append([xx, yy, s+1])
                holds.remove((xx,yy))
if step : print(min(step))
else : print(-1)