import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
honey_rooms = dict()    # 딕셔너리를 이용해서 만들어보자
honey_rooms_list = list()
for j in range(0, M + 1):
    for i in range(0, N + 2):
        honey_rooms[(i, j)] = 0

for j in range(1, M + 1):
    for i in range(1, N + 1):
        honey_rooms_list.append((i, j))

K = int(input())
hole = list()   # 리스트를 순회하며 구멍 값을 0으로 바꿔줄 것
for i in range(K):
    x1, y1 = map(int, input().split())
    hole.append((x1, y1))

for honey_room in honey_rooms_list: # 이 과정이 시간이 많이 걸릴 것으로 추정된다...
    if honey_room in hole:
        honey_rooms_list.remove(honey_room)
# print(honey_rooms_list)

honey_rooms[(1, 1)] = 1

for room in honey_rooms_list:
    x, y = room
    if y % 2:
        honey_rooms[(x, y)] += honey_rooms[(x - 1, y - 1)] + honey_rooms[(x, y - 1)] + honey_rooms[(x - 1, y)]
        honey_rooms[(x, y)] %= 10 ** 9 + 7
    else:
        honey_rooms[(x, y)] += honey_rooms[(x, y - 1)] + honey_rooms[(x - 1, y)] + honey_rooms[(x + 1, y - 1)]
        honey_rooms[(x, y)] %= 10 ** 9 + 7
print(honey_rooms[(N, M)])