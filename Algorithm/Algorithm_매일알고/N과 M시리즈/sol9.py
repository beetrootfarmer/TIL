import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = []
arr = sorted(list(map(int, input().split())))
visited = [False] * N
seq = []

def dfs():
    # 중복되는 수열 확인
    if len(seq) == M:
        print(*seq)
        return
    rmb = 0
    for i in range(N):
        if not visited[i] and rmb != arr[i]:
            visited[i] = True
            seq.append(arr[i])
            rmb = arr[i]
            dfs()
            visited[i] = False
            seq.pop()
dfs()