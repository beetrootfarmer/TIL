#테스트 케이스마다 a+b 출력
#0,0이 입력되면 while문 종료
a = int()
b = int()
while (0 < a, b < 10) : 
    a ,b = map(int,input().split())
    if (a==0) & (b==0) :
        break
    else : print(a+b)
