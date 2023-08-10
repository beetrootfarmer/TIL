import sys
import time
input = sys.stdin.readline

# __입력
K, N = map(int,input().split())                       # K : 오영식이 이미 가지고있는 랜선 1~10000
                                                      # N : 필요한 랜선의 개수 1~1000000 && K이상의 수
lans = [int(input()) for _ in range(K)]                # 이미 가지고 있는 랜선 각각의 수
# __출력
# 랜선 N개를 만들 수 있는 최대 랜선의 길이 (정수)

# 근사치 길이 알고리즘
# 1. 전체 랜의 길이를 더해서 N으로 나누고
# 2. 1의 값을 줄여 나가면서 가능한 랜의 길이를 찾는다?
    # 가능한 랜의 길이란 랜 배열을 순회하면서 1의 값으로 나눠서 N이 나오는지 확인

# 0.00025sec
# lenlan = sum(lans) // N                                # 231
# nn = 0
# while True:
#     sumslicing = sum(list(map(lambda x: x//lenlan, lans)))
#
#     if sumslicing == N: break
#     elif sumslicing < N: lenlan -= 1
#     else : lenlan += 1
# print(lenlan)

s = time.time()
# 이분탐색을 이용하는 방법
# 0.00023 sec
start , end = 1, max(lans)              # 시작과 끝을 1과 가장 긴  랜선의 길이로 설정한다
while start <= end:                     # start가 end와 같거나 더 커지면 end를 출력한다
    mid = (start + end) // 2            # 시작과 끝의 평균을 mid 변수에 담는다
    lenlan = 0                          # mid의 길이일 때 총 몇개의 랜선이 나올 수 있는지 확인할 변수 lenlan
    for i in lans:
        lenlan += i // mid              # 랜선의 길이를 mid로 나누고 lenlan에 더한다
    if lenlan >= N:                     # lenlan이 필요한 N과 같거나 N보다 크다면 start 지점을 mid 뒤로 보낸다
        start = mid + 1
    else:                               # N보다 작으면 end 지점을 mid 앞으로 보낸다
        end = mid -1
    print(start, mid, end)
print(end)

e = time = time.time()
print(f"{e - s:.5f} sec")
# 12.07 12:30 ~
# 4 11
# 802 4개 200.5
# 743 3개 247.6
# 457 2개 228.5
# 539 2개 269.5