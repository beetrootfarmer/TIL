# 입력 : 정사각 배열의 길이 N과 이동할 숫자의 개수 K
#        숫자X와 X를 이동할 지점 (R, C)
# 출력 : X를 (R, C)로 이동하는데 필요한 표의 회전 수를 줄 별로 출력

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, K = map(int,input().split())

table = [0] * N
a, b = 1, 1
for i in range(N):
    table[i] = list(range(a, (N*b)+1))
    a += N
    b += 1

def turn_the_table(op, now, to, table):
    global turn, N
    while now != to:
        turn += 1
        l = table[op].pop()
        table[op] = [l] + table[op]

        if now == N - 1:
            now = 0
        else:
            now += 1


# table에서 X 의 Row 좌표를 찾는 함수
def searchRC(X, table):
    global N
    rr, cc = 0, 0
    for i in range(N):
        if X in table[i]:
            rr = i
            for j in range(N):
                if table[i][j] == X:
                    cc = j
    return (cc, rr)


for _ in range(K):
    X, R, C = map(int,input().split())
    r_to, c_to = R-1, C-1
    r_now, c_now = searchRC(X, table)

    turn = 0                     # 회전 수 0으로 초기화
    turn_the_table(c_now, r_now, r_to, table) # 가로세로 변경하는 것 함수화

    spin_table = list(map(list, zip(*table)))# 배열 행과 열 뒤집기
    rr, cc = searchRC(X, spin_table)
    turn_the_table(cc, c_now, c_to, spin_table)
    table = list(map(list,zip(*spin_table)))
    # print(*table)
    print(turn)