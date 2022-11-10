import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
B = False

while t:
    if not B:
        p += 1
        q += 1
        if p == w and q == h-1:        # 45도 위로 올라가다가 코너를 만났을 떄
            p, q = w-1, h
            B = True
            t -= 1
        elif p == w-1 and q == h:
            p, q = w, h-1
            B = True
            t -=1
        elif p == w or q == h:
            B = True
    else:
        p -= 1
        q -= 1
        if p == 1 and q == 0:
            p, q = 0, 1
            B = False
            t -= 1
        elif p == 0 or q == 0:
            B = False
    t -= 1
print(p, q)