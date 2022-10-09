import math
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
girl = [0 for _ in range(7)]
boy = [0 for _ in range(7)]
for i in range(N):
    s, y, = map(int, input().split())
    if s: boy[y] += 1
    else: girl[y] += 1

cnt = 0

def count_std(std, K):
    global cnt
    if std > K:
        cnt += math.ceil(std/K)
    elif std:
        cnt += 1

for i in range(1, 7):
    # i 는 학년
    count_std(girl[i], K)
    count_std(boy[i], K)
print(cnt)