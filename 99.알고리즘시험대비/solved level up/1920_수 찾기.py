N = int(input())
A = set(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))
for i in range(M):
    if search[i] in A:
        print(1)
    else:
        print(0)

# A를 set으로 받지 않으면 시간초과