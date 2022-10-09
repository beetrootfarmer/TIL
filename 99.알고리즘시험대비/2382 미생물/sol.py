import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    C = [[0]*N for _ in range(N)]
    # C = [[0] for _ in range(N)]
    msm = [0 for _ in range(K)]
    direction = [0,(-1, 0), (1, 0), (0, -1), (0, 1)]
    opposit = [0,2, 1, 4, 3]

    for k in range(K):
        msm[k] = list(map(int, input().split()))        # 리스트 형태로 받음 (i, j, m, d) (세로, 가로, 미생물 수 , 이동방향)
    stack =[]
    for m in range(M):                                  # M시간만큼 반복
        for k in range(K):                              # 이동이 한번에 이뤄지고 변환! 미생물 군집 수 K만큼 이동하는 for문
            if msm[k] == 0: continue
            i, j, m, d = msm[k]
            i += direction[msm[k][3]][0]
            j += direction[msm[k][3]][1]
            if type(m) == tuple:
                m = m[0]
            if i in (0, N-1) or j in (0, N-1):          # 위치가 가장자리인지 확인
                m //= 2
                d = opposit[d]
            msm[k] = [i, j, (m, m), d]                  # 중복 위치 검사할 때 미생 물 수를 확인하기위해 tuple로 보내줌
            stack.append((i, j, k))                     # 중복 위치 검사를 위해 인덱스번호와 함께 보내줌
        while stack:
            i, j, k = stack.pop(0)
            if msm[k] == 0: continue                    # 이미 중복 자리의 군집이어서 0으로 바뀐 자리
            for a in range(len(stack)):
                if (i, j) == (stack[a][0], stack[a][1]):
                    kk = stack[a][2]                    # 위치가 겹치는 비교군 군집의 인덱스 kk
                    if msm[kk] == 0: continue           # 비교군 군집이 이미 중복이어서 0으로 바뀌었으면 continue
                    tm, m = msm[k][2]                   # tm은 total 미생물 수 , m은 중복이었을 때 군집 중 가장 큰 미생물 수
                    d = msm[k][3]                       # 현재 방향
                    comm = msm[kk][2][0]                # 비교군 군집의 미생물 수
                    tm += comm                          # total 미생물 수에 비교군 군집의 미생물 수를 더함
                    if comm > m:                        # 중복된 상태에서 가장 큰 미생물 수와 비교군 군집의 미생물 수 비교. 비교군이 더 클때
                        m = msm[kk][2][1]               # m 갱신
                        msm[k][3] = msm[kk][3]          # d 갱신
                    msm[kk] = 0                         # 비교군 k에 합쳐졌으니까 제거
                    msm[k][2] = (tm, m)                 # k의 미생물 total, 가장 큰 미생물 수 갱신
    while 0 in msm:
        msm.remove(0)
    result = 0
    for m in msm:
        if type(m[2]) == tuple:
            result += m[2][0]
        else:
            result += m[2]
    print(f'#{tc} {result}')



