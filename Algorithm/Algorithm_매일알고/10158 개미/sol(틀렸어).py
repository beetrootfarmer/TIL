import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
B = False

move = min(w-p, h-q)


def letsmove(move, p, q):
    direction = t // move
    rest = t % move
    if rest == 0:
        if direction % 2:
            print(p, q)
        else:
            print(p - move, q - move)
    elif direction % 2:
        print(p - rest, q - rest)
    else:
        print(p + rest, q + rest)


if move > t:
    print(p+t, q+t)
else:
    p += move
    q+= move
    t -= move
    if (w -2 == h) and ((p, q) in [(w-1, h), (w, h-1), (w-3, h)]):
        cycle = h*6
        move = t%cycle
        if move == 0 : print(p, q)
        else:
            if p == w-1: p, q = w, h-1
            if p == w: p, q = w-1, h
            move -= 1
            B = True
            while move:
                if not B:
                    p += 1
                    q += 1
                    if p == w and q == h - 1:  # 45도 위로 올라가다가 코너를 만났을 떄
                        p, q = w - 1, h
                        B = True
                        move -= 1
                    elif p == w - 1 and q == h:
                        p, q = w, h - 1
                        B = True
                        move -= 1
                    elif p == w or q == h:
                        move = True
                else:
                    p -= 1
                    q -= 1
                    if p == 1 and q == 0:
                        p, q = 0, 1
                        B = False
                        move -= 1
                    elif p == 0 and q == 1:
                        p, q = 1, 0
                        B = False
                        move -= 1
                    elif p == 0 or q == 0:
                        B = False
                move -= 1
            print(p,q)


    else:
        letsmove(min(p, q), p, q)