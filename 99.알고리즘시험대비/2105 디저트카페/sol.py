import sys
sys.stdin = open('input.txt')
# 대각선으로 가능한 경우 모두 탐색해야겠다..

def search_routh(sti, stj, i, j, squre):
    # squre
    global N, already, visited
    if squre and sti == i and stj == j:
        dessert = len(already)
        if dessert %2 == 0 and dessert >= 4:
            d.append(dessert)
        dessert = 0
        squre = []
        return
    else:
        for m in range(4):
            ii, jj = move[m][0] +i, move[m][1] +j
            if 0<=ii<N and 0<=jj<N and not visited[ii][jj] and cafe[ii][jj] not in already:
                if (move[m] not in squre) or (squre[-1] == move[m]):
                    squre.append(move[m])
                    already.append(cafe[ii][jj])
                    visited[ii][jj] = 1
                    search_routh(sti, stj, ii, jj, squre)
                    visited[ii][jj] = 0
                    already.pop()
                    squre.pop()
        else:
            return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    move = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    max_dessert = 0
    already = []
    for i in range(N):
        for j in range(N):
            visited = [[0]*N for _ in range(N)]
            d = []                            # 현재 위치에서 가능한 루트 담는 리스트
            already = []                      # 이미 먹은 거 중복 검사용
            search_routh(i, j, i, j, [])
            if d and max(d) > max_dessert:
                max_dessert = max(d)
    if not max_dessert:
        max_dessert = -1
    print(f'#{tc} {max_dessert}')

