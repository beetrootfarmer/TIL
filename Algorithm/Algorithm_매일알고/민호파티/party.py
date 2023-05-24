import sys

input = sys.stdin.readline

N, people = map(int, input().split())

timetable = []
for i in range(N):
    timetable.append(list(map(int,input().split())))

# 최단시간 찾기. 직통 거리와 모든 좌표의 경유 거리를 비교
for k in range(N):                                      # 경유지
    for i in range(N):
        for j in range(N):
            straight = timetable[i][j]                  # 바로 연결된 길
            via = timetable[i][k] + timetable[k][j]     # 경유하는 길
            if straight > via:
                timetable[i][j] = via

# 결과 출력
for p in range(people):
    s, d, t = map(int, input().split())
    if timetable[s-1][d-1] <=t:
        print('Enjoy other party')
    else:
        print('Stay here')
