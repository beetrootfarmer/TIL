# 입력 : 정사각 배열의 길이 N과 이동할 숫자의 개수 K
#        숫자X와 X를 이동할 지점 (R, C)
# 출력 : X를 (R, C)로 이동하는데 필요한 표의 회전 수를 줄 별로 출력


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N, K = map(int,input().split())

data = []
for _ in range(K):
    X, R, C = map(int,input().split())
    data.append([X, (X-1)//N , (X-1) % N  , R-1, C-1]) # X//N  # [6, 1, 1, 3, 2]

# 타겟을 목표 지점으로 옮기는 함수
def move_target(n, t, N):
    moved = 0 
    if n < t:               # 현재위치 n이 타켓 t보다 앞쪽에 위치하면 이동값은 t-n
        moved += t-n
    elif n > t:             # 현재 위치가 타켓 뒤라면 한바퀴 돌아서 이동해야하기때문에 N - n + t
        moved += N - n
        moved += t
    return moved

def turn_the_table(d):
    global turn, N

    x, rn, cn, rt, ct = data[d]

    mr = move_target(rn, rt, N)
    mc = move_target(cn, ct, N)
    turn = turn + mc + mr       # 움직인 횟수만큼 turn 변수에 반영

    for d2 in range(d+1, K):
        if data[d2][0] == x:
            data[d2][1] = rt
            data[d2][2] = ct
        else:
            if data[d2][1] == rn:
                data[d2][2] += mc
                if data[d2][2] >= N:
                    data[d2][2] = data[d2][2] % N
            if data[d2][2] == ct:
                data[d2][1] += mr
                if data[d2][1] >= N:
                    data[d2][1] = data[d2][1] % N

for d in range(K):
    turn = 0
    turn_the_table(d)
    print(turn)