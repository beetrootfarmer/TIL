import sys
sys.stdin = open('input.txt')

board = [[0 for _ in range(101)] for _ in range(101)]
result = 0
for s in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1
for r in board:
    result += sum(r)
print(result)