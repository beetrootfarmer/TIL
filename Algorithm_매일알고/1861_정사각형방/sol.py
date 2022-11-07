import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**7)
T = int(input())

def gogo(i, j,blocked):
    global move
    if blocked == 4:
        return
    # 한 칸마다 네 방향을 모두 조사해야함
    for d in range(len(dir)):
        ni, nj = i + dir[d][0], j + dir[d][1]
        # 이동했을 때 인덱스번호가 유효하면
        # 이동했을 때 방의 번호가 1 크다면 이동
        if 0 <= ni < N and 0 <= nj < N and rooms[ni][nj] - rooms[i][j] == 1:
            move += 1
            gogo(ni, nj, 0)
        else:
            blocked+=1
            if blocked == 4:
                gogo(i, j, 4)


for tc in range(1, T+1):
    N = int(input())                # N^2개의 방이 N * N 형태로 있음
    rooms = [[] for _ in range(N)]
    for i in range(N):
        rooms[i] = list(map(int, input().split()))
    max_rooms = 0
    start = 0
    dir = [(0,1), (1, 0), (0, -1), (-1,0)]
    for i in range(N):
        for j in range(N):
            move = 1
            gogo(i, j, 0)
            if move > max_rooms:
                max_rooms = move
                start = rooms[i][j]
            if move == max_rooms:
                start = start if rooms[i][j] > start else rooms[i][j]

    print(f'#{tc} {start} {max_rooms}')
