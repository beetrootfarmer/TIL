import sys
input = sys.stdin.readline
# 일곱난장이를 찾아라
# 아홉 난장이의 키를 입력받아 합이 100인 난장이의 키를 오름차순으로 출력
nines = sorted([int(input()) for i in range(9)])
checked = [False] * 9
result = []
def dfs(nans:list):
    sn = sum(nans)
    ln = len(nans)
    if result:return
    if(sn > 100 or ln > 7):return
    if(sn == 100 and ln == 7):
        for i in range(9):
            if checked[i]:
                result.append(nines[i])
        return
    else:
        for i in range(9):
            if not checked[i]:
                checked[i] = True
                dfs(nans+[nines[i]])
                checked[i] = False
dfs([])
for i in result:
    print(i)

