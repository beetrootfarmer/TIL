a, b = map(int, input().split())
# 최대공약수 : 공통 약수 중 가장 큰 것
# a, b 중 작은것으로부터 1까지로 나누면서 나눠지면 break
Divisor = min(a,b)
for mm in range(Divisor, 0, -1):
    if a%mm == 0 and b%mm == 0:
        Divisor = mm
        break
# 최소공배수 : 최대공약수로 나눈 값을 곱한 것
Multiple = Divisor * (a//Divisor) * (b//Divisor)
print(Divisor, Multiple)
