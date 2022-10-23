# 소문자로 만들어진 단어 입력받아서 해당 알파벳이 포함되어있는지 확인
w = list(input())
#ascii_lowercase로 알파벳 리스트 만들기
from string import ascii_lowercase
asc  = list(ascii_lowercase)

#알파벳의 위치 리스트 
alp= list()
for i in asc:
    if i in w:
        # w.index(i) : word에서 i가 어디에 위치하는지
        alp.append(w.index(i))
    else : alp.append(-1)
# 알파벳이 포함되어있다면 위치 출력
# 단어에 포함되어있지 않다면 -1 출력
for i in alp:
    print(i, end=' ') # print는 자동 줄바꿈, end='' 로 설정하면 줄 안바꾸고 출력 가능