import sys
sys.stdin = open('input.txt')
T = int(input())


def explosionable(at, ato):
    # 선이 겹치는가?

    # 지점까지 같은 시간이 걸리는가?
    # 둘다 통과하면 true 반환
# 3. 1.5초 후에도 만나야함
    pass


for tc in range(1, T+1):
    N = int(input())
    atoms = []
    dir = {0:(0,1), 1:(0,-1), 2:(1,-1), 3:(1,1)}

    for a in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append([x, y, d, k])

    result = 0
    # 1. 원자 한 개에서 나머지 원자를 순회하면서 충돌이 발생하는지 확인한다
    # 2. 충돌이 발생하면 충돌이 발생하는 ( 지점과 시점 )을 리스트에 담고 두 원자는 폭파시키고 result에 에너지를 담아둔다

    for a in range(N-1):
        for a2 in range(a+1, N):
            pass
            if atoms[a] and atoms[a2]:
                if explosionable(atoms[a] , atoms[a2]):
                    # explosion.append()=
                    # atoms[a] = atoms[a2] = 0
                    pass
    print(f'#{tc} {result}')

