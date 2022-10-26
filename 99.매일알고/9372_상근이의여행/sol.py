import sys
sys.stdin = open('input.txt')


def popping(area, i, j):
    pass
# popping을 하는 2차원 배열을 탐색 할 때마다 새로 만들어줘야하나????


def dfs(i):
    pass
    global N, W, H
#   N개의 구슬을 쏘는 모든 경우의 수를 탐색
    if i == N:
        return
    for i in range(W):
        for j in range(H):
            if data[j][i]:
                popping(data[i][j]-1, i, j)

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, W, H = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    dfs(0)

    # 남은 블럭의 개수를 출력