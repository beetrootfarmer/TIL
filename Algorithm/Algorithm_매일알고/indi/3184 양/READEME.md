# 문제
- 커다란 영역이 주어지고 그 안에서 이동가능한 작은영역 여러개가 있다
- 작은 영역 안에서 늑대와 양의 수를 세어서 양>늑대 일 경우 양이 남고 나머지의 경우 늑대가 남는다
---
# 알고리즘
1. 2차원배열로 주어진 커다란 영역을 순회하며 방문하지 않고, #(울타리)가 아닌 인덱스를 담아 moon 함수로 보낸다
2. moon 함수에서 받은 인덱스를 큐에 담고 상하좌우를 순회하며 v, o를 count 하는데
3. 새로 이동한 인덱스는 q에 담아서 2를 반복한다
4. 작은 영역을 다 확인하면 늑대와 양의 수를 비교해서 결과에 반영한다
---
# 코드
```python
import sys
from collections import deque
sys.stdin = open('input.txt')

R, C = map(int, input().split()) # R은 가로 C는 세로
data = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
move = [(1, 0),(0, 1),(-1, 0),(0, -1)]
result = [0, 0]
def moon(i, j):
    global lamb, wolf
    q = deque()
    q.append((i, j))
    if data[i][j] == 'v':
        wolf += 1
    elif data[i][j] == 'o':
        lamb += 1
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        # 사방이 막혀있을 경우 본인 카운트 해야함
        for m in move:
            ii, jj = m[0]+i, m[1]+j
            if 0 <= ii < R and 0 <= jj < C and data[ii][jj] != '#' and not visited[ii][jj]:
                if data[ii][jj] == 'v':
                    wolf += 1
                elif data[ii][jj] == 'o':
                    lamb += 1
                visited[ii][jj] = 1
                q.append((ii, jj))


for i in range(R):
    for j in range(C):
        if not visited[i][j] and data[i][j] != '#':
            lamb, wolf = 0, 0

            moon(i, j)
            if not lamb and not wolf:
                continue
            elif lamb > wolf:
                result[0] += lamb
            else:
                result[1] += wolf
print(*result)

```