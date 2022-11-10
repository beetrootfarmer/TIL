import sys
sys.stdin = open('input.txt')

def preorder(n):
    global N
    if n > N:
        return
    else:
        preorder(n*2)
        print(data[n], end='')
        preorder(n*2 +1)

for tc in range(1, 11):
    N = int(input())
    data = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        l = list(map(str,input().split()))
        data[i] = l[1]
    # print(data)
    print(f'#{tc}', end=' ')
    preorder(1)
    print()
