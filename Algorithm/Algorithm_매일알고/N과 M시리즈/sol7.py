import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
def dfs():
    if len(ans) == M:
        print(" ".join(list(map(str,ans))))
        return
    for i in arr:
        # 내림차순도 가능함
        ans.append(i)
        dfs()
        ans.pop()
dfs()