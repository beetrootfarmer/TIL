#테스트 케이스마다 a+b 출력
#0,0이 입력되면 while문 종료

while 1 : 
    try :
        a ,b = map(int,input().split())
        print(a+b)
    except :
        break