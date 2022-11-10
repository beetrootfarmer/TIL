import itertools
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synrgy = [list(map(int, input().split())) for _ in range(N)]
    # 1.
    # 리스트에 있는 대칭점들(Sij, Sji) 을 합해서 Sij에 저장
    # (0, 1) ~ (0, N-1), (1, 2)~(1, N-1), (2, 3) ~(2, N-1) ...
    for i in range(N - 1):
        for j in range(i + 1, N):
            synrgy[i][j] += synrgy[j][i]

    # 2.
    # comb : range(0, N) 숫자들로 N//2개의 조합을 만들어 저장한 리스트
    data = list(range(0, N))
    comb = list(itertools.combinations(data, N // 2))

    # 3.
    # comb을 순회하면서 요리마다의 합을 구해서 C에 저장
    C = [[] for _ in range(len(comb))]
    for c in range(len(comb)):
        # 4.
        if len(comb[c]) > 2:
            lst = list(itertools.combinations(comb[c], 2))
            C[c] = 0
            # 4-1.
            for l in lst:
                i, j = l
                C[c] += synrgy[i][j]
        # 5.
        else:
            i, j = comb[c][0], comb[c][1]
            C[c] = synrgy[i][j]

    #6.
    # C 숫자들 중 최소 차이를 출력
    min = 20000
    lc = len(C)
    cross = lc - 1
    # print(len(comb))
    # 7.
    # ! 대칭되는 인덱스의 comb 조합에 중복되는 요소가 없음
    # 두 개의 요리에 같은 요리를 쓸 수 없는데 조합을 만들었을 떄 양 끝에 있는 조합이 숫자가 전혀 겹치지 않
    for i in range(lc // 2):
        diff = abs(C[i] - C[cross])
        if diff < min:
            min = diff
        cross -= 1
    print(f'#{tc} {min}')