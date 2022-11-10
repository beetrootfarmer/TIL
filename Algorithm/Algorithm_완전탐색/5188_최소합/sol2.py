T = int(input())

def dfs(i, j, n):
    global ms, ns
    if ms < ns:                             # 현재 합이 최소 합보다 크면 탐색 중단 return
        return
    if i == n and j == n:
        if ms > ns:
            ms = ns
    else:
        for m in move:
            ii, jj = i+m[0], j+m[1]
            if 0<=ii<=n and 0<=jj<=n:
                ns += arr[ii][jj]
                dfs(ii, jj, n)
                ns -= arr[ii][jj]
        

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ms = N*N*10                             # 최소 합 ms에 전체 칸의 숫자가 10일 때가 최대값으로 초기화
    ns = arr[0][0]                          # 탐색마다 값을 더해줄 현재 합 
    move = [(1, 0), (0, 1)]                 # 오른쪽이나 아래로만 이동
    # visited = [[0]*N for _ in range(N)]     # 방문 표시 할 리스트
    dfs(0, 0, N-1)
    print(f'#{tc} {ms}')
