import sys
input=sys.stdin.readline

N, K = map(int, input().strip().split())
start = list(range(1, N+1))
dead = []
for i in range(1, N+1):
    d = len(start)%(i+K)
    dead.append(start.pop(d))
