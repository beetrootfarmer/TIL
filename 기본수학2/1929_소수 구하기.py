# # m이상 n이하의 소수를 한줄에 하나씩 출력하시오
# m , n= map(int,input().split())

# for i in range(m,n+1):
#     e = 0
#     if i > 1 : #1은 소수가 아니기 때문에 제외하고 만들어줘야함 
#         for n in range(2,i):
#             if i % n == 0:
#                 e += 1
#                 break
#         if e == 0:
#             print(i)

#=========================위에꺼 시간초과=========================
m , n= map(int,input().split())

for i in range(m,n+1):
    for N in range(2,i):
        if i%N ==0:
            break
        elif i%N != 0 and N == i-1:
            print(i)
#=========================또 시간초과=========================
import sys
m,n = map(int, sys.stdin.readline().split())

for i in range(m,n+1):
    for N in range(2,i):
        if i%N ==0:
            break
        elif i%N != 0 and N == i-1:
            print(i)   

#=========================함수 만들기=========================
#=========================에라토스테네스의 체로 풀었을 때 시간초과가 나지 않는다
#=========================에라토스테네스의 체 : 소수의 배수는 약수로 무조건 x를 포함한다
#===============================================따라서 절대 소수의 배수는 소수가 될 수 없다는 규칙
#=========================루트를 씌워서 약수 확인? num**0.5 = num루트

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): #여기서 num이 약수가 있다면 거기까지만 적용!
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
        

