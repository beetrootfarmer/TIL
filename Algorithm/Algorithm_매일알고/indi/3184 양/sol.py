import sys
from collections import deque

sys.stdin = open('input.txt')

R, C = map(int, input().split()) # R은 가로 C는 세로
data = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
move = [(1, 0),(0, 1),(-1, 0),(0, -1)]
result = [0, 0]
# print(*data)
# print(*visited)
# print(data[0][9])
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
