import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int,input().split())))
seq = ''
dit = {}
temp = []
def dfs(i:int, dep:int):
    if dep == M:
        seq = ' '.join(map(str,temp))

        if seq not in dit:
            dit[seq] = 1
            print(seq)
        return
    for j in range(i,N):
        temp.append(arr[j])
        dfs(j, dep+1)
        temp.pop()
dfs(0, 0)