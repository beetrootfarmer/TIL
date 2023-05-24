import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
sequence = []

def dfs():
    if len(sequence) == M:
        print(" ".join(list(map(str,sequence))))
        return
    for i in arr:
        if i not in sequence:
            sequence.append(i)
            dfs()
            sequence.pop()

dfs()