import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

T = int(input())

def stack_box(r, c, h, box_count):
    global highest

    if box_count == box:
        highest = max(h, highest)
        return

    # 현재 바닥 상자 가로 세로보다 초과하면 상자를 회전해서 체크
    for bo in range(box):
        i, j, k = data[bo]
        if used[bo] :
            continue
        used[bo] = 1
        for (a, b, d) in [(i, j, k), (j, k, i), (k, i, j)]:
            if(a > r) or (b > c):
                continue
            stack_box(a, b, d + h, box_count + 1)
        else:
            stack_box(r, c, h, box_count+1) # 현재 상자가 올라갈 수 없는 경우 상자 카운트만 하고 다시 호출
        used[bo] = 0


for tc in range(1, T+1):
    box = int(input())
    data = []
    highest = 0
    for b in range(box):
        r, c, h = map(int, input().split())
        data.append((r, c, h))
    # 상자를 쌓는 모든 경우의 수를 확인
    # 6(상자 하나당 면적 경우의 수)**상자개수
    used = [0] * box
    # 모든 상자를 6면 회전하면서 쌓아서 확인
    for bo in range(box):
        r, c, h = data[bo]
        used[bo] = 1
        for (a, b, d) in [(r, c, h), (c, h, r), (h, r, c)]:
            stack_box(a, b, d, 1)
        used[bo] = 0
    print(f'#{tc} {highest}')

#1 76
#2 158
#3 1181
#4 6897
#5 36700