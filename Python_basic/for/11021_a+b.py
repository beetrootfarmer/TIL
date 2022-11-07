import sys

T = int(input())  # 테스트 케이스

for x in range(1,(T+1)) :
    a,b = map(int, sys.stdin.readline().split())
    if (0< a,b <10) : 
        print("Case #"+str(x)+":", a+b) 
        #x를 문자형과 붙여쓰기 위해서는 str(x)로 형변환하고 + 사용하기 
    elif (x==T) : break
    else : ("0과 10 사이의 숫자를 입력하세요")