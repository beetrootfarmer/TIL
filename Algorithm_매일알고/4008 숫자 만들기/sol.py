import sys
sys.stdin = open('input.txt')

T = int(input())


# def product(arr,r, N):
#     for i in range(N):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in product(arr,r-1, N):
#                 yield [arr[i]] + next
def dfs(r, i):
    global mx, mn, N

    if i == N:
        if r > mx : mx = r
        if r < mn : mn = r
        return
    for o in range(4):
        if OP[o]:
            if o == 0:
                OP[o] -=1
                dfs(r+NB[i], i+1)
                OP[o] += 1
            elif o == 1:
                OP[o] -=1
                dfs(r-NB[i], i+1)
                OP[o] += 1
            elif o == 2:
                OP[o] -=1
                dfs(r*NB[i], i+1)
                OP[o] += 1
            else:
                OP[o] -= 1
                dfs(int(r / NB[i]), i + 1)                  # 나눗셈 연산에서 소숫점 자리 제거
                OP[o] += 1
    return

for tc in range(1, T+1):
    N = int(input())                                        # N 숫자의 개수
    OP = list(map(int, input().split()))                    # 연산자의 개수 리스트
    NB = list(map(int, input().split()))                    # N개의 숫자 리스트
    mx = -1000000000
    mn = 1000000000
    # arr = product(o, N-1, N-1)
    # arr = set(list(map(tuple, arr)))
    # 계속 중복 순열로 해결하려다가 안돼서 dfs로 바꿈
    dfs(NB[0], 1)                                           # 첫번째 숫자에서 시작하고 1번 인덱스부터 확인

    print(f'#{tc} {mx - mn}')
