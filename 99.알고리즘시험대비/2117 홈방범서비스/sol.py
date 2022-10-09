
# 마름모 사이즈 k를 1부터 시작해서 늘려나간다
# 최소 필요한 집부터 시작해서 손해보지 않는 지점까지 탐색
# 최소 필요한 집 = 운영비용 이상인 M의 배수 중 가장 작은 수
# 지도를 순회하면서 어디 위치에서 마름모를 그려야 많은 집을 포함하는지 확인한다
import copy
import sys
sys.stdin = open('input.txt')

def security_service(i, j, k,N):
    if k == 1:
        return village[i][j]
    # 현재 위치를 더해주고
    else:
        home = village[i][j]
        visited[i][j] = 1

        i -= 1
        home += village[i][j]
        move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 이 순서로 사각형을 그릴것임
        # 점점 더 큰 마름모 사각형을 그리기
        for kk in range(k):
            for m in move:
                for _ in range(kk):  # 그려야하는 마름모의 길이만큼 반복해서 i, j좌표를 이동한다
                    i, j = i + m[0], j + m[1]
                    if 0 <= i < N and 0 <= j < N and not visited[i][j]:
                        home += village[i][j]
                        visited[i][j] = 1
                        # if i ==10 and j == 10 and k==N+1:
                        #     print('?!?')
            i -= 1
        return home

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(N)]
    served = 0

    # # 최소로 필요한 집은 k/M(올림)
    for k in range(1, N+2):                             # k = 1   # 마름모 크기
        for i in range(N):
            for j in range(N):
                visited = [[0]*N for _ in range(N)]
                home = security_service(i, j, k,N)
                rev = M * home                          # 리턴받은 가구수 * 가구당 수입
                pr = rev - ((k**2) + ((k-1)**2))        #  수익 - k크기에 따른 운영비용

                if pr >= 0 and home>=served:              # 수익이 있을 때 profit 에 제공받은 가구수 비교하고 갱신
                    served = home
                    # result = copy.deepcopy(visited)
                    # result.append([i, j])
                    # print(k)
                    # for n in range(N):
                    #     print(visited[n])
                    # print()

    print(f'#{tc} {served}')
    # for n in range(N):
    #     print(village[n])
    # print()
    # for n in range(N+1):
    #     print(result[n])
    # print()
