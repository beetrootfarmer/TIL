import sys

input = sys.stdin.readline

T, W = map(int,input().split())
tree = []                       # 자두가 떨어지는 나무 리스트
yam = 0                         # 먹은 자두 갯수
for t in range(T):
    tree += [int(input())]

j = [0]*T

def jadu(move,now,n):
    global yam, j
    if n != T and move ==W:
        if tree[n] != now:
            jj = sum(j)
            if jj > yam:
                yam = jj
            return
    if move == W and n == T:
        jj = sum(j)
        if jj > yam:
            yam = jj
            # print(j)
        return

    if n == T:
        return

    for i in range(n,T):
        if not j[i]:
            j[i] = 1
            if tree[i] == now:
                jadu(move, now, i+1)
            else:
                if now == 1:
                    jadu(move+1, 2, i+1)
                else:
                    jadu(move+1, 1, i+1)
            j[i] = 0
            # move -= 1

jadu(0,1,0)
print(yam)