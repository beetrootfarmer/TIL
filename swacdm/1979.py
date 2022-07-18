test_case = int(input())
for case in range(test_case):
    N , K = map(int,input().split()) #N = board size, K = line size
    board = []
    hor_cnt , ver_cnt, answer = 0
    for i in range(N):
        board[i].append(list(map(int,input().split())))
    for v in range(0,N): #(0,len(board)):
        ver = [0]*N
        for h in range(0,N): #board[v]:
            if board[v][h] == 1 :
                hor_cnt += 1
                ver[h] += 1
            elif hor_cnt == K:
                answer += 1
                hor_cnt = 0
            elif ver[h] == K:
                answer += 1
                ver[h] = 0