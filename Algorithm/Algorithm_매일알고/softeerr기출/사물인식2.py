import sys

sys.setrecursionlimit(10 ** 8)

# -1000~1000까지 이므로 최대 넓이가 4*10^6입니다.
answer = 4 * (10 ** 6)


def dfs(num, K, minX, minY, maxX, maxY, color):
    global answer
    # 모든 색을 다 포함했다면 답과 비교해줍니다
    if num > K:

        X = abs(maxX - minX)
        Y = abs(maxY - minY)
        now = X * Y
        print('num ',num, ', now ', now, ', maxX, minX', maxX, minX, ', maxy, minY ', maxY, minY)
        if answer > now:
            answer = now
        return
    # 사실 K개의 색이 모두 있으므로 굳이 if를 표시 안해도 되지만, 꼼꼼하게 할려면 이게 맞을듯합니다.
    if color[num]:
        for nx, ny in color[num]:

            NminX = min(minX, nx)
            NmaxX = max(maxX, nx)
            NminY = min(minY, ny)
            NmaxY = max(maxY, ny)
            tx = NmaxX - NminX
            ty = NmaxY - NminY
            temp = tx * ty
            # 현재까지의 넓이가 answer보다 작으면 dfs를 돌려줍니다
            # 굳이 지금 answer보다 큰 데 굳이 더 돌려주면서 시간초과 나는 것보다는 나으니깐.
            if answer > temp:
                dfs(num + 1, K, NminX, NminY, NmaxX, NmaxY, color)


N, K = map(int, input().split())
color = [[] for _ in range(K + 1)]

for _ in range(N):
    x, y, k = map(int, input().split())
    color[k].append((x, y))

# 1번색 좌표 각각마다 dfs시작점으로 잡아줌
for x, y in color[1]:
    dfs(2, K, x, y, x, y, color)

print(answer)