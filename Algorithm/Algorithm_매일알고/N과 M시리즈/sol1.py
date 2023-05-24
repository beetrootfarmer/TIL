import itertools
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
permute = list(map(list,itertools.permutations(range(1,N+1), M)))
for p in permute:
    print(*p)