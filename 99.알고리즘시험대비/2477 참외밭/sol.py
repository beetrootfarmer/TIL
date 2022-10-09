import sys
sys.stdin = open('input.txt')

cham = int(input())

farm = [0] * 5
# 1동 2서 3남 4북
empty = 0
a1= a2 = 0
stack = []               # 입력받은 순서대로 넣는 데이터
for _ in range(6):
    d, m = map(int, input().split())
    stack.append([d,m])
    if farm[d]:
        farm[d] = [m, farm[d]]
    else:
        farm[d] = m
# 중복이 없는 방향 두 개가 전체 넓이 A
# print(farm)
# print(empty)
for i in range(5):
    if type(farm[i]) != list:
        if a1: a2 = farm[i]
        else: a1 = farm[i]
longlong = []
start_longlong = 0
for i in range(6):
    if stack[i][1] in (a1, a2):
        start_longlong = i
        if i+1 < 6 and stack[i+1][1] in (a1, a2):
            i += 1
        break
i += 1
for _ in range(4):
    longlong.append(stack.pop(i))

A = a1*a2
empty =longlong[1][1] * longlong[2][1]

print(cham*(A-empty))