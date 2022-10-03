# import sys
# sys.stdin = open('input.txt')

# def dfs(d, n):
#     if d == 3:                  # 3개를 찾으면
#         if check# 연속인 숫자인지 확인 

def is_run_triplet(arr, n):
    for i in range(n):
        if arr.count(arr[i]) == 3:
            return True
    arr = sorted(arr)
    i = 0
    while i < n-2:
        if arr[i]+1 in arr and arr[i]+2 in arr:
            return True
        i += 1
    # trplt = dfs(0, n)            # run 확인하는 dfs
    # if trplt: return True

    return False

T = int(input())
for tc in range(1, T+1):
    IN = list(map(int, input().split()))
    plyr1 = []
    plyr2 = []
    result = 0
    for i in range(6):
        plyr1.append(IN[i*2])
        l = len(plyr1)
        if l >=3 and is_run_triplet(plyr1, l):
            result = 1
            break
        plyr2.append(IN[i*2+1])
        l = len(plyr2)
        if l >=3 and is_run_triplet(plyr2, l):
            result = 2
            break
    
    print(f'#{tc} {result}')
    
    