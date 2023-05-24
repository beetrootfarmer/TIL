import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []

def dfs(i , combi):
    if len(combi) == M and combi not in result:
        print(*combi)
        result.append(combi)
        return
    for j in range(i, N):
        dfs(j+1, combi+[arr[j]])
dfs(0, [])
