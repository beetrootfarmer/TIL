import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int,input().split())))
# N개 수로 만들 수 있는 M길이의 수열을 출력
# 중복된 수열 출력x
# 수열을 오름차순으로 출력
# result = []
# def dfs(seq:list):
#     if len(seq) > M or seq in result:
#         return
#     if len(seq) == M and seq not in result:
#         result.append(seq)
#         print(*seq)
#         return
#     else:
#         for i in range(N):
#             dfs(seq+[arr[i]])
# dfs([])
# -------시간초과---------
dict = {}
lst = []
def dfs(dep:int):
    if dep == M:
        seq = ' '.join(map(str,lst))
        if seq not in dict:
            dict[seq] = 1 # 중복확인을 리스트가 아닌 딕셔너리 키값으로 해서 시간을 줄임
            print(seq)
        return
    for i in range(N):
        lst.append(arr[i])
        dfs(dep+1)
        lst.pop()
dfs(0)

