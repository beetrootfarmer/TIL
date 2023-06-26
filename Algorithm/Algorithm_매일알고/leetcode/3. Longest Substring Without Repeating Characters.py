# 입력받은 스트링을 순회하면서 최대 가능한 중복없는 부분문자열을 확인
# 2point 활용
# O(N + N)
from collections import deque
def lengthOfLongestSubstring(string):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    # 1) 중복 제거 후 몇개의 알파벳이 있는지 확인(최대 길이임으로 한번 경우를 찾으면 탐색종료하기위함)
    cntAlpha = len(set(list(string)))
    # 2) 맨처음 글자부터 문자열을 순회하며 최대글자수 확인 & 리턴값 갱신
    lenStr = len(string)
    i, s = 0, deque()
    maxLen = 0
    if lenStr <= 1:
        return lenStr
    while i < lenStr:
        if result == cntAlpha:
            maxLen = result
            break

        if string[i] not in s:
            s.append(string[i])
            result += 1
        else:
            maxLen = max(result, maxLen)
            while string[i] in s:
                s.popleft()
                result -= 1
            s.append(string[i])
            result += 1

        i += 1
    return max(result, maxLen)

a = lengthOfLongestSubstring("aab") # aab pwwkew
print(a)