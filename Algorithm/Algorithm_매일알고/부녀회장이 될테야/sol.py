import sys
input = sys.stdin.readline

T = int(input())
search = []
mk,mn = 0,0

# abc = [[1, 2, 3], [4, 5, 6]]
# print(abc[1][0:2])
# print(sum(abc[1][0:2]))

for tc in range(T):
    k = int(input())            #   층
    n = int(input())            #   호
    search.append((k, n))

    mn = max(n,mn)
    mk = max(k,mk)

apt = [list(range(1,mn+1))]      #   0층 초기화 1~가장큰 호 ... [1,2,3,4,5,6,7]
for a in range(1,mk+1):            #   가장 높은 층만큼 반복하면 값을 구해놓기
    floor = [0]*mn
    for b in range(mn):          #    0~가장 큰 호-1 ... 0,1,2,3,4,5,6
        if b>0:
            floor[b] = floor[b-1] + apt[a-1][b]
        else:
            floor[b] = 1

    apt.append(floor)

for k,n in search:
    print(apt[k][n-1])
