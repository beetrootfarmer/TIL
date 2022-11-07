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
    # 1. 주변 8점에 지로가 없는 지점을 탐색 후 count
        # 1-2. 해당 지점 주변의 8곳을 채우기
        # 1-3. 이걸 재귀로 반복해서 연속 open될 수 있는 모든 지점을 탐색
    # 2. 연속 open이 안되는 나머지 지점에 대해 count
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
    