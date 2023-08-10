import sys
input = sys.stdin.readline

N = int(input())


def print_stars(n):
    if n == 1:
        return ['*']
    Stars = print_stars(n//3)
    S = []

    for star in Stars:
        S.append(star*3)
    for star in Stars:
        S.append(star+' '*(n//3)+star)
    for star in Stars:
        S.append(star*3)
    return S

print('\n'.join(print_stars(N)))