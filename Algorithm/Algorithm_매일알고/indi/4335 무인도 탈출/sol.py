import sys
from itertools import combinations
# input = sys.stdin.readline
sys.stdin = open('input.txt')

T = int(input())
def stack_stack(stack_box):
    global highest

    def f(s, e):
        global highest
        if s == e:
            for sb in range(len(stack_box)):
                a, b, c = stack_box[sb]
                for combi in combinations([a, b, c], 3):
                    # combi로 만든 것 중 높이가 가장 높은 것?
                    #
                    # if highest != 0:
                    #     if(combi[0] <= a) and (combi[1] <= b):
                    #         h += combi[2]
                    # else:
                    #     i, j, h = combi
                    print(list(combi))

            #     b, b2, c = stack_box[sb]
            #     h2 = 0
            #     for combi in combinations([b, b2, c], 3):
            #         k, l, h3 = combi
            #         if (k <= b) and (l <= a2):
            #             h2 = max(h2, h3)
            #     h += h2
            # highest = max(highest, h)
        else:
            for j in range(s, e):
                p[s], p[j] = p[j], p[s]
                f(s + 1, e)
                p[s], p[j] = p[j], p[s]

    if len(stack_box) == 1:
        highest =  max(stack_box)
    else:
        p = stack_box
        f(0, len(p))




for tc in range(1, T+1):
    box = int(input())
    data = []
    highest = 0
    for b in range(box):
        r, c, h = map(int, input().split())
        data.append((r, c, h))
    # 상자를 쌓는 모든 경우의 수를 확인
    # 6(상자 하나당 면적 경우의 수)**상자개수
    # 모든 상자를 3면 회전하면서 쌓아서 확인 (90도씩만 회전 가능)

    # 비트 연산자로 다시 도전
    for i in range(0, (1 << box)):
        stack_box = []
        for j in range(0, box):
            if i & (1 << j):
                stack_box.append(data[j])
        if stack_box:
            stack_stack(stack_box)
    print(f'#{tc} {highest}')

#1 76
#2 158
#3 1181
#4 6897
#5 36700