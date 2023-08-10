
def security_service(i, j, k):
    global N
    if k == 1:
        return village[i][j]
    else:
        home = village[i][j]
        visited[i][j] = 1
        i -= 1
        home += village[i][j]
        for kk in range(k):                                     # 마름모의 크기 k만큼
            for m in move:                                      # 점점 더 큰 마름모 사각형을 그리기
                for _ in range(kk):
                    i, j = i + m[0], j+m[1]
                    if 0 <= i < N and 0 <= j < N and not visited[i][j]:
                        home += village[i][j]
                        visited[i][j] = 1
            i -= 1                                              # 바깥 마름모를 그릴때 i 좌표 한칸 위로 
        return home

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    village = [list(map(int,input().split())) for _ in range(N)]
    user = 0
    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    for k in range(1, N+2):                                     # N + 2 :  마을 전체를 덮을 수 있는 마름모크기의 최대
        for i in range(N):
            for j in range(N):                                  # 마을의 모든 좌표를 순회하면서 마름모를 그릴 것
                visited = [[0] * N for _ in range(N)]
                home = security_service(i, j, k)
                profit = (home * M) - ((k**2) + ((k-1) ** 2))   # 가구 수 당 비용 - 총 운영비용 
                if profit >= 0 and home>=user:                  # 수익이 있고 유저수가 더 많으면
                    user = home                                 # 갱신
    print(f'#{tc} {user}')

    
    