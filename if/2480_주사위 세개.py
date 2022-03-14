# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 
# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

a, b, c = map(int, input().split())
reward = int(0)

#같은 눈 세 개의 경우 10,000원+(같은 눈)×1,000
if a == b == c : reward += 10000 + (a*1000)

if (a == b and a != c) or (a == c and a != b)  : reward += (1000 + (a*100))
if (b == c and b != a) : reward += (1000 + (b*100))

if (a != b and a != c and b != c) : 
    if a > b and a > c : reward += a*100
    if b > a and b > c : reward += b*100
    if c > a and c > b : reward += c*100
print (reward)
