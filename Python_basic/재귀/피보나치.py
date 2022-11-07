def fibo(n):
    if (n <= 1):
        return (n)
    else :
        return (fibo(n - 1) + fibo(n - 2))
n = int(input())
print(fibo(n))

#  if문을 탈때까지 재귀가 돌아가고 
# if문을 타면 n 이 1인 상태부터 재귀에 걸린 것이 순차적으로 실행된다