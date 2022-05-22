import sys
from collections import Counter
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
ac = Counter(a).most_common() #2중배열로 어떤'수'가 '몇회' 나왔는지 들어감
print(round(sum(a) / n)) # a의 sum()의 평균값을 반올림 round()
print(a[n // 2])
if len(ac) > 1: #입력한 수 가 2개이상일 때 
    if ac[0][1] == ac[1][1]: #두 수의 빈도가 같으면 두번쨰로 작은 수를 출력하라는 조건
        print(ac[1][0])
    else:
        print(ac[0][0])
else:
    print(ac[0][0])
print(a[-1] - a[0]) #마지막인덱스 a[-1]에서 첫번째 인덱스 수 빼기
