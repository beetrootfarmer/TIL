## 문제 
- '*' 은 지뢰 , '.'은 지뢰가 없는 곳
- '.'을 클릭했을 때 사방에 지뢰가 없으면 연속으로 클릭된다(지뢰찾기 게임 룰과 동일)
---
## 접근방법
- 1. 주변에 지뢰가 없는 지점을 선택한다
    - count를 1 올리고 좌표 주변에 연속으로 open 가능한 부분을 visited[]에 표시한다 
    - visited[]를 활용하여 선택한 좌표 주변을 dfs로 채운다
    - 이때 해당 좌표가 0일때만 깊이 탐색을 이어간다
- 2. 연속 open이 안된(visited가 0이고 '.'인 지점)을 count한다
---
## 코드
```python
import sys
sys.stdin = open('input.txt')
T = int(input())


def is_zero(i, j,N):
    for a in around:
        ii, jj = i + a[0], j + a[1]
        if 0<=ii<N and 0<=jj<N:
            if popping[ii][jj] != '.':
                return False
    return True


def fill_around(i, j, N):
    for a in around:
        ii, jj = i+a[0], j+a[1]
        if 0<=ii<N and 0<=jj<N:
            if popping[ii][jj] == '.' and not visited[ii][jj]:
                visited[ii][jj] = 1
                if is_zero(ii, jj, N):
                    fill_around(ii, jj, N)

for tc in range(1,T+1):
    N = int(input())
    popping = [list(input()) for _ in range(N)]
    around = [(-1,-1), (-1,0), (-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if popping[i][j] == '.' and not visited[i][j] and is_zero(i, j ,N): # 1
                count += 1
                visited[i][j] = 1
                fill_around(i, j, N) # 1-2, 1-3
        # print(visited[i])
    for i in range(N):
        for j in range(N):
            if popping[i][j] == '.' and not visited[i][j]:
                count += 1
    print(f'#{tc} {count}')
    
```