import sys
sys.stdin = open('input.txt')

for _ in range(4):
    aj, ai, aj2, ai2, bj, bi, bj2, bi2 = map(int, input().split())
    # a 직사각형 b선분 c점 d공통부분 없음

    # 1. 공통부분이 없을 때
    # 첫번째 사각형 기준으로 왼쪽/ 오른쪽/ 위/ 아래 있을 때. 네 가지 경우
    if aj>bj2 or aj2<bj or ai2 <bi or ai>bi2:
        result = 'd'
    # 2. 점만 겹쳐있을 때. 네 가지 경우
    elif (ai == bi2 and (aj == bj2 or aj2 == bj)) or \
            (ai2 == bi and (aj2 == bj or aj == bj2)):
        result = 'c'
    # 3. 선이 겹쳤을 때.
    elif aj2 == bj or ai2 == bi or aj == bj2 or ai == bi2:
        result = 'b'
    else:
        result = 'a'
    print(result)
    # 배열을 만드는 방식으로 하면 메모리 초과가 납니다
    # 쉽게 생각합시다
    # 겹칠 수 있는 선도 4가지 경우 입니다...

        # 뻘짓한 흔적...
        # S = [[0]*(aj2+1) for _ in range(ai2+1)]
        # for j in range(aj, aj2+1):
        #     for i in range(ai, ai2+1):
        #         S[i][j] = 1
        # dupl = [[] for _ in range(2)]
        # for i in range(bi, bi2+1):
        #     for j in range(bj, bj2+1):
        #         if i <= ai2 and j <= aj2 and S[i][j]:
        #             dupl[0].append(i)
        #             dupl[1].append(j)
        # dupl[0] = len(set(dupl[0]))
        # dupl[1] = len(set(dupl[1]))
        # if (dupl[0] == 1 and dupl[1] > 1) or (dupl[0] > 1 and dupl[1] == 1):
        #     result = 'b'
        # else:
        #     result = 'a'
