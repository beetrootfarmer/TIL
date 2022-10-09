import sys
sys.stdin = open('input.txt')
# sys.setrecursionlimit(10**7)
def pipe_n(dir,pipe):
    v, r = dir[0], dir[1]
    # dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if pipe == 1:
        return 1
    elif pipe == 2:
        if (v, r) in [(0, 1), (0, -1)]:
            return 1
    elif pipe == 3:
        if (v, r) in [(1, 0), (-1, 0)]:
            return 1
    elif pipe == 4:
        if (v, r) in [(-1, 0), (0, 1)]:
            return 1
    elif pipe == 5:
        if (v, r) in [(1, 0), (0, 1)]:
            return 1
    elif pipe == 6:
        if (v, r) in [(-1, 0), (0, 1)]:
            return 1
    elif pipe == 7:
        if (v, r) in [(0, -1), (-1, 0)]:
            return 1
    else:
        return 0
def pipe_a(dir, pipe):
    v, r = dir[0], dir[1]
    # dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if pipe == 1:
        return 1
    elif pipe == 2:
        if (v, r) in [(0, 1),(0, -1)]:
            return 1
    elif pipe == 3:
        if (v, r) in [(1, 0),(-1, 0)]:
            return 1
    elif pipe == 4:
        if (v, r) in [(1, 0), (0, 1)]:
            return 1
    elif pipe == 5:
        if (v, r) in [(0, -1), (-1,0)]:
            return 1
    elif pipe == 6:
        if (v, r) in [(0, -1),(1 , 0)]:
            return 1
    elif pipe == 7:
        if (v, r) in [(0, 1), (1, 0)]:
            return 1
    else:
        return 0


def dfs(i, j, dep):
    global ti, tj, time
    # dfs 방향을 모두 탐색
    # 방문한 곳은 visited 표시하고 다시 가지 않도록
    if dep == time:
        return
    for d in range(4):
        di, dj = i + dir[d][0], j + dir[d][1]
        pipe_now = ternel[i][j]
        if not pipe_n(dir[d],pipe_now):
            continue
        if 0 <= di < ti and 0 <= dj < tj:
            pipe_next = ternel[di][dj]
            if pipe_next and visited[di][dj] == 0 and pipe_a(dir[d], pipe_next):
                visited[di][dj] = 1
                dfs(di, dj, dep + 1)


T = int(input())
for tc in range(1, T+1):
    tj, ti, mj, mi, time = map(int, input().split())
    # 터널의 크기 ti, tj
    # 맨홀 지점 mi, mj
    # 주어진 시간 time
    # 위치할 수 있는 장소를 터널 배열에 visited 표시
    ternel = [[] for _ in range(ti)]
    visited = [[0]*tj for _ in range(ti)]
    for i in range(ti):
        ternel[i] = list(map(int,input().split()))
    # print(*ternel)
    dir = [(1,0),(0,1),(-1,0),(0,-1)]

    dfs(mi, mj, 0)
    area = 0
    print(visited)
    for i in range(ti):
        area += visited[i].count(1)
    print(f'#{tc} {area}')

