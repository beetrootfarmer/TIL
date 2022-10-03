T = int(input())

def dfs(t, total, m, n):
    global mw
    if t >= m-1 or used.count(1) ==N:
        if total > mw:
            mw = total
    else:
        for w in range(n):
            if T[t] >= full[t] + W[w] and not used[w]:
                used[w] = 1
                full[t] += W[w]
                dfs(t, total+W[w], m, n)
        else:
            dfs(t+1, total, m, n)

for tc in range(1, T+1):
    N, M = map(int ,input().split())            # 화물 수, 트럭 수
    W = list(map(int, input().split()))         # 화물의 무게
    T = list(map(int, input().split()))         # 트럭의 적재 용량

    W = sorted(W, reverse=True)                 # 화물의 적재용량이 큰 것 순으로 정렬하고 순회
    T = sorted(T, reverse=True)                 # 트럭의 적재용량이 큰 것 순으로 정렬
    # 하나도 올리지 못할 경우는 0 을 리턴
    used = [0] * N                              # 무거운 화물을 적재하고, 사용한 화물에는 used 표시
    full = [0] * M                              # 화물이 다 찼을 때 ..?
    mw = 0                                      # 적재할 수 있는 최대 중량
    dfs(0, 0, M, N)                           # 트럭 인덱스, 현재 적재 총합, 트럭 수, 화물 수
    print(f'#{tc} {mw}')