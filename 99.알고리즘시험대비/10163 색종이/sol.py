import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0]*1001 for _ in range(1001)]               # 가로세로 1001까지
for num in range(1,N+1):
    a, b, w, h = map(int, input().split())
    p, q = a+w, b+h
    for i in range(b, q):
        arr[i][a:p] = [num]*w
for n in range(1, N+1):
    num = 0
    for i in range(1001):
        num += arr[i].count(n)
    print(num)