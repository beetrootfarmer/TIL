#  2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
# 이러한 수를 골드바흐 수라고 한다.

# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
# 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

#소수 배열을 만들어놓고 테스트
import math
def primeNum(n):
  for i in range(2,int(math.sqrt(n))+1):
      if n%i==0:
        return False
  return True # 소수이면 트루


t = int(input()) #테스트 케이스 
while(t):
    num = int(input()) #2보다 큰 짝수 n
    cha =[10000, 0, 0]
    for n in range(1,(num//2)+1):
        if primeNum(n) and primeNum(num-n): # 두 수가 소수이면
            n1, n2 = n, num-n
            chacha = n2 -n1
            if n > num-n :
                chacha = n1 - n2

            if cha[0]>chacha:
                cha = [chacha, n1, n2]
    print(cha[1],cha[2])
    t -= 1


    # ============위에꺼 시간초과임============

t = int(input()) #테스트 케이스 

def primeNum(n):
# True False 모두 리턴하지 않고 True일때만 return!
    f = False
    for i in range(2,int((n**0.5))+1):
        if n%i==0:
            f = True
            break
    return f # 소수이면 트루

for _ in range(t): #while 대신 for문
    num = int(input()) #2보다 큰 짝수 n
    ##둘로 나눈 수에서 한칸씩 옮기면서 소수를 찾는방식
    a = num // 2
    b = a
    while(primeNum(a) or primeNum(b)): 
        a-=1
        b+=1
    print(a,b)
# ============math 사용 유무 시간차이 : 
#                math.sqrt()대신 (n**0.5) 썼을 때 20ms 빠르다 ============
import math  
t = int(input()) #테스트 케이스 

def primeNum(n):
# True False 모두 리턴하지 않고 True일때만 return!
    f = False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            f = True
            break
    return f # 소수이면 트루

for _ in range(t): #while 대신 for문
    num = int(input()) #2보다 큰 짝수 n
    ##둘로 나눈 수에서 한칸씩 옮기면서 소수를 찾는방식
    a = num // 2
    b = a
    while(primeNum(a) or primeNum(b)): 
        a-=1
        b+=1
    print(a,b)          

