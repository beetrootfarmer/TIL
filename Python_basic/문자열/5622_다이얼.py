# 다이얼 전화
# 1을 누르는데 2초 2=>3초 3=>4초 ... 9=>10초
# 각 자리에 적힌 알파벳에 맞는 번호를 입력
grand = list(input().lower())
time=0
for i in grand:
    #or 연산자는 타입 비교 연산자..?
    # 
    if i =='a'or i =='b'or i =='c': time += 3
    elif i == 'd'or i =='e'or i =='f': time += 4
    elif i =='g'or i =='h'or i =='i': time += 5
    elif i == 'j'or i =='k'or i =='l': time += 6
    elif i == 'm'or i =='n'or i =='o': time += 7
    elif i == 'p'or i =='q'or i =='r'or i =='s': time += 8 
    elif  i == 't'or i =='u'or i =='v': time += 9
    else : time += 10
print(time)

#다른사람 답
number = input()
li = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
result = 0
for i in number:
    for x in range(0,26):
        if i == chr(x+65): #65=A 66=B ... 
            result = result + li[x]
print(result)
