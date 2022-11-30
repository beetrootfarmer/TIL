import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # office = [0]*N
    exit = []
    people = []
    for n in range(N):
        d = list(map(int,input().split()))
        # office[n] = d
        for j in range(N):
            if d[j] > 1:
                exit.append((n, j, d[j]))
            if d[j] == 1:
                people.append((n, j))

    # 사람마다 가까운 계단을 찾는다
    # 3명이 초과되는 계단이 있다면 다른 계단으로 갔을 때 거리+대기시간+계단길이를 비교
    # 사람별로 가까운 계단 정보를 저장
    stair = [0] * len(people)
    ecounter = [0] * len(exit)
    for p in range(len(people)):
        r, c = people[p]
        for e in range(len(exit)):
            sr, sc, ss = exit[e]
            cha = (abs(r-sr) + abs(c-sc))
            # 만약 이미 그 계단에 사람이 꽉찼으면..
            if ecounter[e]>3:
                continue
            if (ecounter[e] == 3):
                # 대기시간포함 계산해서 계단을 선택
                sl = N
                for s in stair:
                    if s and s[1] == ss:
                        sl = min(sl, s[2])
                # 대기시간 = (sl + ss) - cha
                wait_time = abs((sl + ss) - cha)
                stair[p] = [e, ss, cha, wait_time]
                ecounter[e] += 1
            else:
                if stair[p] == 0:
                    stair[p] = [e, ss, cha, -1]
                    sl = cha+ss
                    ecounter[e] += 1
                elif stair[p][3] >= 0:
                    # 대기시간 비교
                    if (cha + ss) < (stair[p][3] + stair[p][1] + stair[p][2]):
                        stair[p] = [e, ss, cha, -1]
                        ecounter[stair[p][0]] -= 1
                elif sl > cha+ss:
                    ecounter[stair[p][0]] -= 1
                    stair[p] = [e, ss, cha, -1]
                    sl = cha+ss
                    ecounter[e] += 1


    # office = [list(map(int,input().split())) for _ in range(N)]
    # print(*office)
    # print(people)
    # print(exit)
    # print(stair)
    onstair = list([] for _ in range(len(exit)))
    # print(onstair)
    time = 0
    while stair.count(0) < len(stair):
        for s in range(len(stair)):
            if stair[s]:
                if stair[s][2]:
                    stair[s][2] -= 1
                else:
                    # 현재 사람이 갈 계단 onstair[stair[s][0]]
                    # 현재 사람이 내려갈 계단 수 stair[s][1]
                    os = onstair[stair[s][0]]
                    if not stair[s][1]:         # 더 이상 내려갈 계단이 없으면
                        onstair[stair[s][0]].remove(s)
                        stair[s] = 0
                    elif s in os:                 # 이미 계단을 내려가고있으면
                        stair[s][1] -= 1
                        # if stair[s][1] == 0:
                        #     onstair[stair[s][0]].remove(s) # 더 이상 내려갈 계단이 없으면
                        #     stair[s] = 0
                    elif len(os) < 3:           # 아직 계단을 내려가지 않았는데 계단에 사람이 3명 미만이면
                        stair[s][1] -= 1
                        onstair[stair[s][0]].append(s)
        time += 1
    print(f'#{tc} {time}')
