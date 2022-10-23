while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    # 3, 4, 5
    # 3**2 + 4**2 = 5**2
    M = max([a, b, c])
    if (M**2)*2 == (a**2 + b**2 + c**2):
        print('right')
    else:
        print('wrong')