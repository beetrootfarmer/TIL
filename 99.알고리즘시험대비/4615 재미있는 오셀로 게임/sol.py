import sys
sys.stdin = open('input.txt')

def count_color(color):
    global N
    result = [0,0]
    for c in range(2):
        for i in range(N):
            result[c] += board[i].count(color[c])
    return result

def do_game(i, j, me):
    global N
    #받아온 자리에 돌을 놔야함
    board[i][j] = me

    if me == 1:
        enem = 2
    else: enem = 1
    # 8 방향을 탐색하면서 상대편 색이 있으면 맞은편에 본인 색이 있는지 확인
    # 내 돌들 사이에 상대편 돌이 여러개 올 수 있음 ㅡㅡ
    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for d in direction:
        s = 0
        s += 1
        ti, tj = i + d[0]*s , j + d[1]*s
        while 0<=ti<N and 0<=tj<N and board[ti][tj] == enem:
            s += 1
            ti, tj = i + d[0] * s, j + d[1] * s
        if 0<=ti<N and 0<=tj<N and board[ti][tj] == me:
            for t in range(1,s):
                board[i+(d[0]*t)][j+(d[1]*t)] = me

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    # 초기 설정
    # N//2 - 1의 인덱스부터 2 , 1
    # N // 2인덱스에 1, 2
    init = N // 2
    board[init-1][init-1] = 2
    board[init-1][init] = 1
    board[init][init-1] = 1
    board[init][init] = 2
    for m in range(M):
        j, i, color = map(int, input().split())
        do_game(i-1, j-1, color)
        # print(board)
    bw = count_color([1,2])
    print(f'#{tc} {bw[0]} {bw[1]}')
