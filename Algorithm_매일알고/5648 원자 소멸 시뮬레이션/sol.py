import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    atoms = []
    x_range = (0, 0)
    y_range = (0, 0)
    dir = {0:(0,1), 1:(0,-1), 2:(1,-1), 3:(1,1)}
    atomsGps = []
    explosion = []

    for a in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append([x, y, d, k])
        x_range = (min(x_range[0], x),max(x_range[1], x))
        y_range = (min(y_range[0], y),max(y_range[1], y))
        atomsGps.append((x, y))
    result = 0
    while True:
        if atoms.count(0) == N:
            break
        for a in range(N):
            if not atomsGps[a] or not atoms[a]:
                continue
            d = dir[atoms[a][2]][0]
            m = dir[atoms[a][2]][1]
            # 이동
            atoms[a][d] += m
            # 인덱스가 넘어갔는지 확인
            if atoms[a][0] not in range(x_range[0], x_range[1]+1) or\
                    atoms[a][1] not in range(y_range[0], y_range[1]+1):
                atoms[a],atomsGps[a] = 0,0
            else:
                atomsGps[a] = [atoms[a][0], atoms[a][1]]
        # 원자가 있는지 확인
        for ag in range(N-1):
            for ag2 in range(ag+1, N):
                if not atoms[ag] or not atoms[ag2]:
                    continue
                if atomsGps[ag] and atomsGps[ag2] and atomsGps[ag] == atomsGps[ag2]:
                    result += (atoms[ag][3] + atoms[ag2][3])
                    atoms[ag][3], atoms[ag2][3] = 0, 0
    print(f'#{tc} {result}')

