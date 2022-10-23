# import sys
# sys.stdin = open('input.txt')

cham = int(input())
# 6개의 데이터를 받을건데
# 12개 길이로 만들어서 찾을거임
# 왜냐면 경사가 있는 부분에서 빈공간이 어디인지 찾기 위함!
farm = [[] for _ in range(12)]
dir = [0]*5
short = []
for i in range(6):
    d, l = map(int, input().split())
    if i>2 and dir[farm[i-1][0]] == 2 and dir[d] == 1:
        short = [farm[i-1][0], d]
        # 빈 공간의 마지막 선임
    dir[d] += 1
    farm[i] = [d, l]
    farm[i+6] = [d, l]
long = []
i = 0
cnt = 0
S = []
while farm[i][0] == short[0] and farm[i][1] == short[1]:
    i+=1
for f in range(i, 12):
    # 여기부터 시작하는거임
    if farm[f][0] not in short:
        if farm[f][1] not in long:
            long.append(farm[f][1])
    else:
        if farm[f][0] in short:
            cnt+=1
        if cnt >1 and len(S)<2:
            S.append(farm[f][1])
    if len(long) == 2 and len(S)==2:
        break
# print('long = ', long)
# print('S = ', S)
# print('short=', short)
result = (long[0]*long[1]) - (S[0] * S[1])
print(result*cham)

