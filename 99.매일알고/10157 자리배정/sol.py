# 6 6
# 0
# 9 64
import sys
sys.stdin = open('input.txt')

def squre(start, row, ver,K):
    # 채워나갈 숫자
    global num
    if num + (ver - start) < K: num += ver - start
    else:
        for i in range(start,ver) : # 왼쪽 세로
            if num == K: return i, start
            arr[i][start] = num
            num += 1
    if num + (row - start -1) < K: num += row - start -1
    else:
        for j in range(start+1,row): # 아래 가로
            if num == K: return ver - 1, j
            arr[ver - 1][j] = num
            num += 1
    if num + (ver - start -1) < K: num += ver - start -1
    else:
        for i in range(ver-2, start-1, -1):       # 오른쪽 세로
            if num == K: return i, row-1
            arr[i][row-1] = num
            num += 1
    if num + (row - start - 2) < K: num += row - start - 2
    else:
        for j in range(row-2,start, -1):         # 윗줄 가로
            if num == K: return start, j
            arr[start][j] = num
            num += 1
    return 0, 0

# T = int(input()) # 테스트케이스 세 개 합침
# 달팽이 문제 활용해서 접근
# for tc in range(1, T+1):
C, R = map(int, input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]
start = 0
i = j = 0
num = 1
if K<0 or (C*R) < K:
    print(0)
elif (C*R) % 2 and K == (C*R):  # 홀수 사이즈인 경우 중앙에 n2만 추가로 채우기
    i = C // 2
    j = R // 2
    print(j+1, i+1)
elif K <= R:
    print(1, K)
else:
    while num <=K:  # //2까지. 인덱스 번호니까 -1
            # 여기서 가지칙기
        if (num + (C-start)*2 + (R-start)*2 -4 -1) >= K:
            i, j = squre(start, C, R, K)
        else:
            num = num + (C-start)*2 + (R-start)*2 -4
        start += 1  # 시작지점 (R-1, 0), (R-2, 1), (R-3, 2)...
        C -= 1
        R -=1
        if i or j:
            break
    print(j+1, i+1)
    for i in range(len(arr)):
        print(arr[i])

