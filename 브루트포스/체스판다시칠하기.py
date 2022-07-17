# 색을 바꾸는 것 1로. (1,1) 원본과 변환 두가지 버전
def change_01(board, ch_board,n):
    if (n == 1): #바꾼버전
        ch_board[0][0] = 1
        if board[0][0] == 'B':
            board[0][0] = 'W'
        else :
            board[0][0] = 'B'
    else:
        ch_board[0][0] = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i]) - 1):
            if (j == 0) and (i > 0):
                if board[i-1][j] == board[i][j] and ch_board[i - 1][j] == 0:
                    ch_board[i][j] = 1
                elif board[i-1][j] != board[i][j] and ch_board[i - 1][j] == 1 and n == 0:
                    ch_board[i][j] = 1
            if board[i][j] == board[i][j + 1] and ch_board[i][j] == 0:
                ch_board[i][j+1] = 1
            elif board[i][j] != board[i][j + 1] and ch_board[i][j] == 1 and n == 0:
                ch_board[i][j+1] = 1
    return(ch_board)
    
    
# 8,8 길이만큼 카운트했을 때 합이 가장 적은 수를 min으로 리턴
def search_min(board, p ,q):
    min = 10000
    for i in range(0, q + 1):
        for k in range(0,p + 1):
            s = 0
            for j in range(i,i + 8):
                s += sum(board[j][k : k + 8]) # board[j]의 합
            if (s < min):
                min = s
    if min == 10000:
        min = 0
    return (min)

y, x = map(int,input().split())
board = [[0]*x for _ in range(0,y)]
for i in range(y):
    board[i] = list(input())

ch_board_ori =[[0]*x for _ in range(0,y)]
ch_board_ch = [[0]*x for _ in range(0,y)]
ch_board_ori = change_01(board, ch_board_ori, 0)
ori_min = search_min(ch_board_ori, x - 8, y - 8)
ch_board_ch = change_01(board, ch_board_ch, 1)
ch_min = search_min(ch_board_ch, x - 8, y - 8)

# 두가지 버전 중 min이 더 작은 것을 출력 
print(ori_min) if (ori_min < ch_min) else print(ch_min)

#=========노가다로 풀었고 테스트케이스 7개 다 잘나오는데 틀렸대;
#서칭해보니까 for문 네 개로 풀길래 다시 해봄ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

y, x = map(int,input().split())
board = []
count = []
for _ in range(y):
    board.append(input())

for i in range(y - 7):
    for j in range(x - 7):
        cntw = 0
        cntb = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        cntw += 1
                    if board[k][l] != 'B':
                        cntb += 1
                else :
                    if board[k][l] != 'B':
                        cntw += 1
                    if board[k][l] != 'W':
                        cntb += 1
        count.append(min(cntw, cntb))
print(min(count))
    