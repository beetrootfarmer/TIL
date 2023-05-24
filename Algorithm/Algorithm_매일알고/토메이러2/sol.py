import sys
from collections import deque

input = sys.stdin.readline

# 익은 토마토에 인접한 토마토는 하루가 지나면 익는다
# 며칠이 지나면 토마토가 모두 익는지
# 최소 일수를 구해라

M, N, H = map(int, input().split()) # 2<= x <= 1000
tomatos = list()
for h in range(H):
    t = list()
    for i in range(N):
        t.append(list(map(int, input().split())))
    tomatos.append(t)

# print(tomatos)
# 1:익은토마토 0:익지 않은 토마토 -1:토마토가 없는칸

days = 0 # 리턴할 일수
red = deque()
x, y, z= 0, 0, 0
# 가로M(x) 세로N(y) 높이H(z)
# 시작한 빨간토마토부터 그 주변으로 1씩 더해가고
# 더 이상 확인할 토마토가 없을 때 전체를 순회하면서 다 익었는지 확인

# 다 익어있는 상태일 경우 확인
green = 0

# 시작 시 담아줄 익은 토마토
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[k][i][j] == 1:
                red.append((k, i, j))
            if tomatos[k][i][j] == 0:
                green += 1

# 모든 토마토가 익어있을 경우 탐색하지 않음
if green == 0:
    print(0)
else:
    # 입력 받은 좌표 기준 여섯 방향을 탐색해서 익은토마토 배열에 담아준다
    def tmt_v(z, x, y):
        for k,i,j in [(0,1,0), (0,0,1), (0,-1,0), (0,0,-1),(-1, 0, 0), (1, 0, 0)]:
            kk, ii, jj = k+z, x+i, y+j
            if 0<=kk<H and 0<=ii<N and 0<=jj<M:
                if tomatos[kk][ii][jj] == 0:
                    red.append((kk,ii,jj))
                    tomatos[kk][ii][jj] = tomatos[z][x][y]+1    # 현재 토마토의 영향을 받아 익는 토마토는 현재값+1을 담아준다

    # 익은토마토 배열이 유효할때 반복
    while red:
        z, x, y = red.popleft()
        tmt_v(z, x, y)

    # 전체 탐색 시 0(안익은 토마토)가 존재하면 return값을 -1로
    for h in range(H):
        for check in range(N):
            if 0 in tomatos[h][check]:
                days = -1

    # 전체가 익은 토마토라면 마지막에 탐색한 익은토마토좌표 -1 값을 리
    if days != -1:
        days = tomatos[z][x][y] - 1
    print(days)
