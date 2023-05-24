import sys
import itertools
from collections import Counter

input = sys.stdin.readline

str = input().rstrip()
strlen = len(str)

# 방문한 문자 확인
lucky = set()
used = [0] * strlen

#
# 입력받은 문자열을 재배치한 모든 경우의 수를 만드는 함수
def cases_string(re_str,re_strlen):
    global str, strlen
    if re_strlen == strlen:
        lucky.add(re_str)
        return

    for i,key in enumerate(str):
        if re_str:
            if key == re_str[-1] or used[i]:
                continue
        used[i] = 1
        cases_string(re_str+key, re_strlen+1)
        used[i] = 0

cases_string('',0)
print(len(lucky))

# counter = Counter(str)
# def cases_string(char,re_strlen):
#     lucky = 0
#
#     # 중복없는 같은 길이의 문자열
#     if re_strlen == strlen:
#         return 1
#
#     # 문자를 순회
#     for key in counter.keys():
#         # 마지막 문자와 입력하려는 문자가 같거나
#         # 이미 모두 사용한 문자일 때 pass
#         if key == char or counter[key] == 0:
#             continue
#
#         # 문자 사용시 counter에서 -1
#         counter[key] -= 1
#         lucky += cases_string(key, re_strlen+1)
#         counter[key] += 1
#
#     # 모든 순회를 마치면 lucky 리턴
#     return lucky
#
# result = cases_string('',0)
# print(result)