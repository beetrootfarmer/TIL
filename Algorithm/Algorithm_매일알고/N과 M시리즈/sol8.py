import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
answer = []
def dfs():
    if len(answer) ==M:
        print(" ".join(list(map(str, answer))))
        return
    for i in arr:
        if not answer or (answer and i >= answer[-1]):
            answer.append(i)
            dfs()
            answer.pop()
dfs()

