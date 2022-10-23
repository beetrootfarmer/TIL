N = int(input())
# 길이가 같으면 사전순으로 l.sort()
L = {n: [] for n in range(51)}
maxlen = 0
for i in range(N):
    a = input()
    la = len(a)
    if a in L[la]: continue
    L[la].append(a)
    maxlen = max(la, maxlen)
for i in range(maxlen+1):
    if L[i]:
        if len(L[i]) > 1:
            L[i].sort()
            for j in L[i]:
                print(j)
        else:
            print(L[i][0])
