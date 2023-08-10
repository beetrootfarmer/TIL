import sys
from collections import deque

input = sys.stdin.readline

# 익은 토마토에 인접한 토마토는 하루가 지나면 익는다
# 며칠이 지나면 토마토가 모두 익는지
# 최소 일수를 구해라

M, N = map(int, input().split()) # 2<= x <= 1000
tomatos = list(list(map(int, input().split())) for i in range(N))
# 1:익은토마토 0:익지 않은 토마토 -1:토마토가 없는칸

days = 0 # 리턴할 일수
red = deque()
x, y= 0,0
# 가로M(x) 세로N(y)
# 시작한 빨간토마토부터 그 주변으로 1씩 더해가고
# 더 이상 확인할 토마토가 없을 때 전체를 순회하면서 다 익었는지 확인

def set_starts():
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 1:
                red.append((i, j))
set_starts()

def tmt_v(x, y):
    for i,j in [(1,0), (0,1), (-1,0), (0,-1)]:
        ii, jj = x+i, y+j
        if 0<=ii<N and 0<=jj<M:
            if tomatos[ii][jj] == 0:
                red.append((ii,jj))
                tomatos[ii][jj] = tomatos[x][y]+1

while red:
    x, y = red.popleft()
    # tomatos[x][y] += 1
    tmt_v(x, y)

for check in range(N):
    if 0 in tomatos[check]:
        days = -1
if days != -1:
    days = tomatos[x][y] -1
print(days)