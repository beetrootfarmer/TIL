# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

#각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
#입력의 마지막에는 0이 주어진다. ==종료 

import sys

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): #여기서 num이 약수가 있다면 거기까지만 적용!
            if num%i == 0:
                return False
        return True

while(True):
    n = int(sys.stdin.readline())
    sosu=[]
    if n == 0:
        break
    for i in range(n+1, (n*2)+1):
        if isPrime(i):
            sosu.append(i)
    print(len(sosu))

    #================== ㅜ위에꺼 또 시간초과====================
    # 범위에 맞는 소수 리스트를 생성해놓고 count해서 값 출력해야함..

import sys
import math

k = 1233456*2+1
all = [1]*k
for i in range(1,k):
    if i == 1:
        continue
    for k in range(2,int(math.sqrt(i))+1):
        if i % k == 0:
            all[i] = 0
            break

while(True):
    n = int(sys.stdin.readline())
    count = 0
    if n == 0:
        break
    for i in range(n+1,2*n+1):
        count += all[i]
    print(count)
