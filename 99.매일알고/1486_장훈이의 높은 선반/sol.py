from itertools import combinations
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, B = map(int,(input().split()))        # N = 직원수, B = 최소 탑 높이
    H = list(map(int, input().split()))
    minsum = sum(H)
    for i in range(1,1<<N):
        t = 0
        for j in range(N):
            if i & (1<<j):                  # 1<<j의 경우에서 i가 1일때
                t+= H[j]
        if t >= B and t-B <= minsum:
            minsum = t-B
    print(f'#{tc} {minsum}')
    # 모든 조합을 최소 탑의 높이와 비교

    # (탑의 높이 - B) 중 가장 차가 작은 것을 출력
