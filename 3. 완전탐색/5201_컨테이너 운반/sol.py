#N개의 컨테이너 무게w, M개의 트럭 적재용량 t
# 제일 쉬운방법? 제일 많이 담을 수 있는 트럭이 제일 무거운 컨테이너를 가져가면 된다
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int,input().split())))  # N개의 화물의 무게
    truck = sorted(list(map(int,input().split())), reverse=True)  # M개의 트럭의 적재용량
    # 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮기고
    # 화물의 전체 무게가 얼마인지 출력
    # 화물을 싣지 못한 트럭이 있을 수도 있고 남는 화물이 있을 수도 있음
    # 컨테이너를 한 개도 옮길 수 없는 경우 0 출력

    # 트럭은 앞에서부터 탐색, 화물은 뒤에서부터 탐색(무거운 것부터)해서 적재되면 pop()
    # used = [False for _ in range(len(w))] # pop() 으로?
    total = 0
    for i in range(len(truck)):
        w_total = 0
        for j in range(len(w)-1, -1, -1):
            if w_total + w[j] <= truck[i]: # and not used[j]:
                w_total += w[j]
                w.pop(j)
                break
                # used[j] = True
        total += w_total
    print(f'#{tc} {total}')

