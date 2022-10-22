width, height = map(int, input().split())
s = int(input())
direction = [0,2, 1, 4, 3]
dir_wh = [0, width, width, height, height]
stores = [0 for _ in range(s+1)]
for i in range(1, s+1):
    a, b = map(int, input().split())
    stores[i] = (a, b)
dongdr, dongds = map(int, input().split())
# 방향이랑 거리가 튜플로 담긴 리스트를 순회하면서 최소 거리 계산!
result = 0
# print(stores)
for i in stores:
    if not i : continue
    # 동근이랑 같은 라인에 있을 떄
    if i[0] == dongdr:
        if dongdr > i[1]:
            result += dongds- i[1]
        else: 
            result += i[1] - dongds
    # 동근이 맞은편에 있을 때 
    elif direction[i[0]] == dongdr:
        # 동근 위치와 남은 범위가 더 큰지, 동근 위치와 경비 범위까지가 더 큰지
        if dongdr in (1, 2):
            result += min((width - dongds + width - i[1]), (dongds + i[1])) + height
        else:
            result += min((height - dongds + height - i[1]), (dongds + i[1])) + width
    elif (dongdr, i[0]) in [(1, 3), (3, 1)]:
        result += dongds + i[1]
    elif (dongdr, i[0]) in [(3, 2), (1, 4)]:
        result += dir_wh[dongdr]-dongds + i[1]
    elif (dongdr, i[0]) in [(2, 3), (4, 1)]:
        result += dongds + dir_wh[i[0]]-i[1]
    else:
        result +=  (dir_wh[dongdr] - dongds) + (dir_wh - i[1])
print(result)