import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

T = int(input())
def fididi(num):
    global found, nlist
    l, r = 0, N - 1             # l과 r의 초기 설정값은 nlist의 1번과 끝번
    flag = -1                   # 숫자가 좌우로 이동하는지 확인할 플래그. 오른쪽으로가면 1 표시 왼쪽으로가면 0 표시
    while l <= r:
        m = (l + r) // 2

        if nlist[m] == num:
            found += 1
            return
        elif num > nlist[m]:    # 중간값보다 숫자가 클때 오른쪽으로
            if flag == 1:
                break
            l = m + 1
            flag = 1            # 이전 탐색때 오른쪽으로 찾았다면 중복되는 것이기 때문에 break
        else:                   # 중간값보다 숫자가 작을 때 왼쪽으로
            if flag == 0:       # 이전 탐색때 왼쪽으로 찾았다면 중복되는 것이기 때문에 break
                break
            r = m - 1
            flag = 0

for tc in range(1, T+1):
    N, M = map(int,input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    nlist.sort()

    found = 0                               # 출력할 숫자. 원하는 조건의 숫자를 찾을때마다 올림


    for num in mlist:                       # mlist 찾아야하는 숫자들을 하나씩 nlist에서 탐색
        fididi(num)                         # 이 부분 함수화하니까 시간초과 9/10 이었던 것 해결됨;'
    print(f'#{tc} {found}')
