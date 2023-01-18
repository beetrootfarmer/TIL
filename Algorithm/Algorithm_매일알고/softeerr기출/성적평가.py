import sys
input = sys.stdin.readline



N = int(input())
# thd = {i : score for i, score in enumerate(list(map(int, input().split())))}
# snd = {i : score for i, score in enumerate(list(map(int, input().split())))}
# fst = {i : score for i, score in enumerate(list(map(int, input().split())))}
fst = list(map(int, input().split()))
snd = list(map(int, input().split()))
thd = list(map(int, input().split()))


def get_the_final_lank():
    answer = [0 for _ in range(N)]
    for lst in [fst, snd, thd]:
        sort_lst = sorted(lst, reverse=True)
        for i in range(N):
            lank = sort_lst.index(lst[i]) + 1
            print(lank, end=' ')
            answer[i] += lst[i]
        print()
    sort_ans = sorted(answer, reverse=True)
    for i in answer:
        print(sort_ans.index(i) + 1, end=' ')

get_the_final_lank()