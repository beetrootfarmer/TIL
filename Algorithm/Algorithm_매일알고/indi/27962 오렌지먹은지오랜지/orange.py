import sys
input = sys.stdin.readline

L = int(input())
str = str(input())

def check_is_orange(a, b):
    if a == b:
        return False
    step = len(a)
    diff = 0
    for i in range(step):
        if(a[i] != b[i]):
            diff+=1
    print(a, b)
    if diff == 1:
        return True
    return False

is_orange = 'NO'
# 탐색범위 1 ~ (문자열길이-1)
for i in range(1, L):
    isOrange = check_is_orange(str[0:i], str[-(i+1):])
    if isOrange:
        is_orange = 'YES'
        break
print(is_orange)