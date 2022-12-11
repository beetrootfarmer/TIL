import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import Counter

def cut_trees(trees, M):               # 함수화 하기전 4536 -> 2156ms으로 시간이 줄어듬..
    l, h = 0, max(trees)  # 초기 가장 낮은값과 높은 값을 나무 높이의 최저, 최고값으로 잡는다.
    # 가장 낮은값을 가장 낮은 나무로 설정하면 틀릴수도 있다 ..
    result = 0

    while l <= h:
        m = (l + h) // 2
        lefts = 0
        for t, cnt in trees.items():
            if t > m:
                lefts += (t - m)*cnt    # counter 컬렉션을 사용해서 같은 높이의 나무는 한번에 계산하도록 처리했을 때 2156 -> 408ms 로 시간이 줄어듬
        if lefts >= M:
            result = m
            l = m + 1
        else:
            h = m - 1
    return result

N ,M = map(int, input().split())
trees = Counter(map(int, input().split()))
print(cut_trees(trees, M))
