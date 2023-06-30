# python split()
# 단어사전을 순회하면서 s를 split 합니다. 마지막에 s 문자열이 모두 제거되면 true를 리턴합니다.
# 단어의 순서에 따라서 통과되지 않을 수도 있기때문에 모든 조합을 검사
# 입력받은 문자열 슬라이스 위치에따라서 join 할 경우 문제를 해결하지못함

# from itertools import permutations
# def wordBreak(s, wordDict):
#     perm = list(permutations(wordDict,len(wordDict)))
#
#     for p in perm:
#         word = s
#         for wd in p:
#             word = ''.join(word.split(wd))
#         if not word:
#             return True
#     return False

    # 단어 s를 순회하면서 글자마다 1~20 마디씩 확인
    # 한번이라도 통과하지 못하면 while문 탈출
    # 시간초과

    # dp 사용해야
def wordBreak(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True

    # 입력받은 문자열 길이만큼 반복
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
a = wordBreak("ddadddbdddadd", ["dd","ad","da","b"])
b = wordBreak('cbca', ["bc", "ca"])
print(a)
print(b)
