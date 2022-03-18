# 몇개의 테스트케이스가 입력될지 

n = int(input())
# 몇개의 점수가 입력될지 숫자와 점수들을 한 리스트에 
for i in range(n) : 
    scr = list(map(int,input().split()))

    sum = 0
    avr = 0
    # scr[0] = 리스트의 길이 -1
    # 입력된 점수들의 평균을 구하고 
    for i in range(1,scr[0]+1) :
        sum += scr[i]
    avr = sum/scr[0]
    # print("avr : " + str(avr))
    o = 0
    # 평균 이상인 점수의 개수
    for i in range(1,scr[0]+1) :
        if scr[i] > avr:
            o +=1
    # 전체의 몇퍼센트를 차지하는지 출력
    # round함수로 소수점 자리수 제한 
    #round(반올림하고자 하는 값, 반올림하는 자릿수)
    p = round((o/(len(scr)-1))*100,4)
    # "{:.1f}".format() 으로 소수점자리 어디까지 출력할지 설정 
    print(str("{:.3f}".format(p))+'%')