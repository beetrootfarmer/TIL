# 이항계수 : 이항식을 이항 정리로 전개했을 때 각 항의 계수
#  주어진 크기의 조합의 가짓수
# 이항? 뽑거나 안뽑거나
# N개 중 K개를 뽑는 이항계수를 구하는 문제

# 내장함수 combinations 사용하기
from itertools import combinations

N, K = map(int, input().split())
combi = list(combinations(range(N)), K)
print(len(combi))

# 파스칼의 삼각형으로 구현하기
def combi(n,k):
    DP = [[0 for _ in range(k+1)] for _ in range(N+1)]
    for i in range(N+1):
        DP[i][0] = 1
    for j in range(K+1):
        DP[j][j] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
    return DP[n][k]

N, K = map(int, input().split())
print(combi(N, K))
#  출처 :https://dailymapins.tistory.com/246