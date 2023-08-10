import sys
sys.stdin = open('input.txt')

def gogo(N, W, H):
    pass
    # 한 줄씩 위에서부터 아래로 탐색하면서 공 쏘기
    #

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, W, H = map(int, sys.stdin.readline().split())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    gogo(N, W, H)

    # 남은 블럭의 개수를 출력