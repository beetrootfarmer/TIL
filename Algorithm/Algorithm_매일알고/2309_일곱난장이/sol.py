# 부분집합의 합이 100인 7개의 조합을 리턴
import itertools
import sys
input = sys.stdin.readline

nans = [int(input()) for _ in range(9)]
combine = list(itertools.combinations(nans, 7))
result = []
for c in combine:
    if sum(c) == 100:
        result = sorted(list(c))
for r in result:
    print(r)