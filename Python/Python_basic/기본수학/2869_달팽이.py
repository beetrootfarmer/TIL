# 땅 위에 달팽이가 있다. 
# V미터 = 달팽이가 올라가는 나무 막대의 높이
# A미터 = 달팽이가 낮에 올라가는 높이
# B미터 = 밤에 잠을 자는 동안 미끄러지는 높이
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
# 2 1 5 => 4
# 5 1 6 => 2
# 100 99 1000000000 => 999999901

A, B, V = map(int,input().split())
# V/ (A-B) 
R = (V-A) / (A-B)
if R<1 : print(2)
else : print(int(R + 1))

#위의 답이 틀렸대..! (VS Code로 돌렸을 떄 예시 답안은 맞았는데)
# math 도구로 나머지 날짜는 올림처리 해줍니다(3일을 넘어가면 4일)
import math

A, B, V = map(int,input().split())
R = math.ceil((V-A) / (A-B))
print(int(R + 1))


# + - V
Dis = 0
Day = 0
# while(True):
#     Dis += A
#     Day += 1
#     if(Dis >= V):
#         break
#     Dis -= B
# print(Day)

# 시간초과
# while(((A-B)*Day)+A < V):
#     Day += 1
# print(Day + 1)

