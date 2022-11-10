#n을 입력받고
n = int(input())
sum = int() 
#1~n까지의 합을 출력 (3일경우 1+2+3 => 출력:6)
for i in range(1,(n+1)):
    sum += i
print(sum)
