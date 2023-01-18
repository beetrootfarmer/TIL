import sys
input = sys.stdin.readline
W, N = map(int, input().split())

def find_the_AMAP(W,N):
    data = {}
    for i in range(N):
        a, b = map(int, input().split())
        if b in data:
            data[b] += a
        else:
            data[b] = a
    result, total = 0, 0
    for value, wei in sorted(data.items(), reverse=True):
        if total + wei > W:
            result += (W - total) * value
        else:
            result += value * wei
            total += wei
    print(result)

find_the_AMAP(W,N)
