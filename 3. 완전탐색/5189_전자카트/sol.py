# 좌표마다 필요한 베터리 사용량이 입력
# 1번은 사무실 2~ N 은 관리구역
# 모든 사무실은 한번씩만..돌아올때도

#
# e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
# e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89
# 이게 이해가 안된다 미쵸...
import sys
sys.stdin = open('input.txt')


def dfs(dep, now, total):
    global min_total
    if dep == n-1:                                                  # 사무실로 되돌아가기 전..
        min_total = min(min_total, data[now][0] + total)          # 현재 합과 min_total 중 작은값으로 min_total을 갱신
        return
    for i in range(1, n):                                         # 사무실 제외 1~ n마지막 방까지
        if not visited[i] and now != i:                           # 현재 경로에서 visited[i]에 방문한 적 없고 (중복X), start(이전 경로와 겹치지 않을 떄)
            visited[i] = 1                                        # 방문 표시 하고
            dfs(dep + 1, i, total + data[now][i])                 # dep 늘리고, 현재 방문 구역 i, 지금까지 총 합
            visited[i] = 0                                        # 경로탐색을 한 번 마칠 경우 visited 다시 0으로


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_total = 1001                                                # 최소합은 100*100 자리에 최소 자연수가 들어왔을때
    dfs(0, 0, 0)
    print(f'#{tc} {min_total}')