# 문제를 똑바로 읽자 
#요리하는데 소요되는 시간은 0~1000분 단위!
H, M= map(int, input().split())
C = int(input())
# (M+C)/60 몫만큼 H에 더하고 나머지가 분
#혹은 C // 60 만큼 더하면 된다
H += C // 60
M += C % 60

#60분 이상이면 분에서 60을 빼고 시간에 1을 더한다
if 59 < M :
    M -= 60
    H += 1
if 23 < H : 
    H -= 24

print(H,M)

#두배는 긴 코드

H, M= map(int, input().split())
C = int(input())
min = M+C
hour = ((M+C)//60)+H

if (0<=H<24) and min<60 : print (H, min)
#요리시간을 더했을 때 60분 이상이면

elif 23 < hour and 59 < min : print(int(hour)-24, int(min)%60)
elif hour < 24 and 59 < min : print(int(hour), int(min)%60) 
else :print("숫자를 똑바로 입력해라")

#잉받는 부분 :  파이썬 몫 기호? // 슬래시 두개!! / 슬래시 하나는 그냥 나누기
