import sys
sys.stdin= open('input.txt')

# - 화물차의 시작시간 기준으로 lambda활용해서 정렬
# - dfs로 끝나는시간 end 이후에(end포함) 시작하는 화물차로 계속해서 탐색해서 개수를 nt로 전달
# - d는 화물차 인덱스 번호

T = int(input())

def dfs(d, end, nt):
    global mt, N
    if d == N-1:
        mt = max(mt, nt)
    else:
        for i in range(d, N):
            if arr[i][0] >= end:
                dfs(i, arr[i][1], nt+1)
        
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[0])            # 시작시간 기준으로 정렬함

    mt = 0
    dfs(0, 0, 0)
    print(f'#{tc} {mt}')
    
        