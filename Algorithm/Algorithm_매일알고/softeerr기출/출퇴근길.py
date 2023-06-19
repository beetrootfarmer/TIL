import sys
input = sys.stdin.readline
# 출퇴근길에 겹치는 접점의 갯수를 출력
# 출근길, 퇴근길 각각에 거치는 접점을 dfs로 파악하고 교집합의 갯수를 출력

n, m = map(int, input().split())
grp = [0] * (n+1)
for _ in range(m):
    s,e = map(int,input().split())
    if grp[s] == 0:
        grp[s] = [e]
    else:
        grp[s].append(e)
S,T = map(int,input().split())

# 가는길, 오는길에 거치는 접접을 담은 리스트
go_back = list()
go_back = [[0] + ([False]*n), [0] + ([False]*n)]

# 리턴값
answer = 0

def dfs(s, e, gb, road):
    global n, go, back, S, T

    if s == e:
        # 목적지에 도착했을 때
        for r in list(set(road)):
            go_back[gb][r] = True
        return
    # 정점을 순회 하면서 방문
    connected = False
    for i in grp[s]:
        connected = True
        if i not in road:
            road.append(i)
            dfs(i,e,gb,road)
            road.pop()

    if not connected and road:
        road.pop()
        dfs(road[-1], e, gb, road)

dfs(S, T, 0, [])
dfs(T, S, 1, [])

for i in range(1, n+1):
    if i == S or i == T:
        continue
    if go_back[0][i] == True and go_back[1][i] == True:
        answer += 1
print(go_back)
print(answer)
