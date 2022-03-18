# 점수/최고점수*100
# s = 점수 몇개 입력할지
s = int(input())
# 점수를 리스트에 받기
scr = list(map(int,input().split()))
maximum = int(max(scr))
# 새로운 시험점수 : maximum / 점수 를 새로운 점수 변수에 더한다
new_scr = int()
for i in range(len(scr)) :
    new_scr += (scr[i]/maximum)*100
# new_scr 점수를 점수 개수로 나누어 평균을 구한다
print(new_scr/len(scr))
