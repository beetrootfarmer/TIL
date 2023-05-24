import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1부터 N까지 자연수 중에 M개를 고른 수열
sequence = []

def dfs():
    if len(sequence) == M:
        print(" ".join(list(map(str,sequence))))
        return
    for i in range(1, N+1):
        if len(sequence) == 0 or sequence[-1] <= i:
            sequence.append(i)
            dfs()
            sequence.pop()
dfs()
