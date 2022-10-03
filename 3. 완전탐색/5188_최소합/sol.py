import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    global min_sum, sub_sum , N
    if min_sum < sub_sum:               # sub_sum을 더하다가 min_sum보다 값이 커지면 가지치기..안해주면 시간초과
        return
    if x == N-1 and y == N-1:           # 목적지
        if min_sum > sub_sum:           # 도착했을 때 합이 min_sum 보다 작으면 갱신
            min_sum = sub_sum

    move = [(1, 0), (0, 1)]             # 오른쪽과 아래로만 움직일 수 있다
    for i in range(2):
        xx, yy = x+move[0][i], y+move[1][i]
        if 0<=xx<N and 0<=yy<N:
            sub_sum += data[xx][yy]
            bfs(xx,yy)
            sub_sum -= data[xx][yy]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 260                       # N의 최대값 13, 10이하의 자연수이므로 최대합은 260...! 250이군요..감사합니다
    sub_sum = data[0][0]                # 부분합
    bfs(0,0)
    print(f'#{tc} {min_sum}')