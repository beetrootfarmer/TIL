
# 크기가 NxN인 체스 위에 퀸N개를 서로 공격할 수 없게 놓는 방법의 수를 구하시오

# 1. 빈 배열을 만든다
# 2. 배열에 숫자를 하나씩 넣으면서 세로확인, 대각선 확인
# 3. 겹치지 않는 위치의 배열이 생성되면 result+1
import sys
input = sys.stdin.readline                                                          # readline으로 바꾸고 pypy로 하니까 시간초과 해결됨
N = int(input())
arr = [-1]*N
result = 0
visited = [False] * N                                                               # 방문한 곳에 또 다시 가지 않도록
def go_queens(queen):
    global N, result

    if queen == N:
        result+=1
        return
    for check_col in range(N):
        if visited[check_col]:
            continue
        can_placed = 1
        for row in range(0, queen):
            if arr[row] == check_col or (abs(queen-row) == abs(check_col-arr[row])): # 2.
                can_placed = 0
                break
        if can_placed:
            arr[queen] = check_col
            visited[check_col] = True
            go_queens(queen+1)
            visited[check_col] = False

go_queens(0)
print(result)