T = int(input())

def dfs(dep, now , ns):
    global ms, N
    # if ns > ms:
    #     return
    if dep == N-1:
        if ms > ns+arr[now][0]:
            ms = ns+arr[now][0]
            print(final, (now, 0))                 # [(0, 2), (2, 1), (1, 3)] (3, 0)
        # ms = min(ms, ns+arr[now][0])            # 돌아온 사무실 값을 더한 ns와 ms를 비교해서 ms 갱신 

    else:
        for i in range(1, N):                   # 관리보호구역 탐색
            if not visited[i] and now!=i:
                visited[i] = 1                  # 방문표시
                final.append((now, i))
                dfs(dep+1, i, ns+arr[now][i])   # 깊이+1, 현재위치 i를 now로 , 현재 합에 위치 값 더해주기
                visited[i] = 0                  # 다른 경로를 탐색하기위해 visited 다시 0으로
                final.pop()

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    ms = 100 * N * N
    final = []
    dfs(0, 0, 0)                            # 탐색 깊이(1~N까지), 이동할때 숫자가 이어짐 now 변수로 이동, 탐색할때마다의 합
    
    print(f'#{tc} {ms}')
    print(final)