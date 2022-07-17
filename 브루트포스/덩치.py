n = int(input())
arr = [[0]*(2) for _ in range(0,n)]
for i in range(n):
    arr[i] = list(map(int,input().split())) #list 형태로 추가할때는 append대신 extendt사용

rank = []
for i in range(0,n):
    rank.append(n)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if (arr[i][0] > arr[j][0]) and (arr[i][1] > arr[j][1]):
            rank[i] -= 1
        elif (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]):
            rank[j] -= 1
        else:
            rank[i] -= 1
            rank[j] -= 1
# 마지막 숫자 제외하고는 개행없이 출력
for i in range(0,len(rank)):
    if (i == len(rank) - 1):
        print(rank[i])
    else: 
        print(rank[i], end=' ')