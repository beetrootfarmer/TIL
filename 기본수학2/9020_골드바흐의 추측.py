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
for i in (0,3):
    num = int(input()) #2보다 큰 짝수 n
    cha =[10000, 0, 0]
    for n in range(1,num):
        if primeNum(n) and primeNum(num-n): # 두 수가 소수이면
            n1, n2 = n, num-n
            if n > num-n :
                chacha = n - (num-n)
            else :
                chacha = (num-n) -n

            if cha[0]>chacha:
                cha = [chacha, n1, n2]
    print(cha[1],cha[2])

    

            

