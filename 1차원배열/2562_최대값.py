# 서로다른 9개의 정수를 입력받고 
# 이중 최댓값과 몇번째 수인지를 출력

#append이용해서 list에 입력값 넣기
list =[]
for i in range(0,9):
    a = input()
    list.append(a)
max = list[0]
for i in range(0,9):
    if list[i] > max :
        max = list[i]
if list[i] == max :
    print(max)
    print(i+1) 

# max()함수와 index()함수로 코드 간결하게 만들기 ㅋㅋ
list = []
for i in range(9) :
    list.append(int(input()))
print(max(list))
print(list.index(max(list))+1)
