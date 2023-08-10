import sys
from collections import deque

input = sys.stdin.readline
# 1. 구슬고르기. 단 첫번째와 마지막은 고를 수 없음
# 2. 구슬의 번호 x. x를 제거
# 3. W(x-1) * W(x+1) 의 에너지 모음
# 4. N을 1감소시키고 구슬을 다시 정렬
# 1~4를 백트래킹으로 반복

N = int(input())
W = list(map(int, input().split()))

picked = [0] * N                            # 방문 확인
energy = 0                                  # 에너지 최대값 확인

def leftPick(x):                            # 사용가능한 왼쪽 구슬을 확인
    if x == 0:
        return W[0]
    for i in range(x,-1, -1):
        if not picked[i]:
            return W[i]

def rightPick(x):                           # 사용가능한 오른쪽 구슬을 확인
    if x == N-1:
        return W[N-1]
    for i in range(x, N):
        if not picked[i]:
            return W[i]

def track_pick(eng):                        # 에너지를 모을 수 있는 여러 경우를 백트래킹으로 탐색한 함수
    global energy
    if 0 not in picked[1:-1]:               # 첫번째와 마지막 제외하고 모두 pick 했다면 값을 확인하고
        if eng >= energy:                   # energy보다 크면 업데이트
            energy = eng
        return

    for i in range(1,N-1):
        if not picked[i]:
            gather = leftPick(i-1)*rightPick(i+1)
            picked[i] = 1
            track_pick(eng+gather)
            picked[i] = 0

track_pick(0)
print(energy)

