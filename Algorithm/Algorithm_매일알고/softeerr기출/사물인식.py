import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dots = [0]*N
answer = 4 * (10 ** 6)                     # 사각형 면적 최대값
# 오답1 : 사각형 면적 최대값이 틀림
# 오답2 : 모서리가 점이 될 필요가 없음(점을 포함하기만 하면 된다. 문제 잘못이해)


for i in range(N):
    x, y, k = map(int,input().split())
    dots[i] = (x,y,k)

# 색이 한 개인 경우
if K == 1:
    answer = 0
else:
    for d in range(N):
        x1, y1, k1 = dots[d]
        for d2 in range(d+1, N):
            x2, y2, k2 = dots[d2]

            minx = min(x1,x2)
            maxx = max(x1,x2)
            miny = min(y1,y2)
            maxy = max(y1,y2)
            width = abs(maxx - minx) * abs(maxy - miny)
            if width < answer:
                include = [k1, k2]
                # 사각형 점 내부에 포함된 점을 탐색
                # x1,x2 범위 내에 있고 y1,y2 범위 내에 있을 경우 포함된 점
                for d3 in range(N):
                    if len(set(include)) == K:
                        break
                    if d3 != d and d3 != d2:
                        x3, y3, k3 = dots[d3]
                        if (minx<=x3<=maxx) and (miny<=y3<=maxy):
                            include.append(k3)

                print(include)
                # 사각형 점과 내부 점을 포함해 모든 색을 가지고있는지 확인
                if len(set(include)) == K:
                # 모든색을 가지고있을 경우 answer보다 작은 값이면 갱신
                    answer = width
print(answer)