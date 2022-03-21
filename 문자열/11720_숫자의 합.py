# 연속으로 입력되는 숫자를 분리해서 이들의 합을 출력하기

#입력될 연속 숫자의 개수
c = input()
#입력되는 연속 숫자를 리스트로 받기
s = list(input())
# 숫자들 더하기
sum = 0
for i in range(len(s)):
    sum += int(s[i])
print(sum)
