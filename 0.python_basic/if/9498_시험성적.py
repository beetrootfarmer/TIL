score = int(input())
# 90 ~ 100점은 A
if 90 <= score <=100 : print('A')
# 80 ~ 89점은 B
elif 80 <= score <=90 : print('B')
# 70 ~ 79점은 C
elif 70 <= score <=79 : print('C')
# 60 ~ 69점은 D
elif 60 <= score <=69 : print('D')
# 나머지 점수는 F
elif 0 <= score <=59 : print('F')
else : print("0에서 100 사이의 수를 입력하세요")