import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def search(A):
    global B
    q = deque()
    q.append((A,""))
    visit = [0] * 10000

    while q:
        a, cmd = q.popleft()
        visit[a] = 1
        if a == B:
            print(cmd)
            break

        # D
        aa = (a*2) % 10000
        if visit[aa] == 0:
            q.append((aa, cmd+'D'))
            visit[aa] = 1
        # S
        aa = (a-1) % 10000
        if visit[aa] == 0:
            q.append((aa, cmd+'S'))
            visit[aa] = 1
        # L
        aa = (10*a + (a//1000))%10000
        if visit[aa] == 0:
            q.append((aa, cmd + 'L'))
            visit[aa] = 1
        # R
        aa = (a//10 + (a % 10) * 1000) % 10000
        if visit[aa] == 0:
            q.append((aa, cmd + 'R'))
            visit[aa] = 1


for tc in range(T):
    A, B = map(int,input().split())
    search(A)
