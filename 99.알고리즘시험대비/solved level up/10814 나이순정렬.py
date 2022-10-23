N = int(input())
# 길이가 같으면 사전순으로 l.sort()
L = {n: [] for n in range(201)}
maxage = 0
for i in range(N):
    age, name = map(str,input().split())
    age = int(age)
    L[age].append(name)
    maxage = max(age, maxage)
for i in range(1, maxage+1):
    if L[i]:
        if len(L[i]) > 1:
            for j in L[i]:
                print(i, j)
        else:
            print(i, L[i][0])
