# 거의 2시간동안 풀었음. 왤케 어렵게 생각했지? 
# 변수를 반복문 내부에 선언하거나 밖에 선언하는것이 헷갈렸던 부분
# 한 시간 지나니까 집중력 바닥나서 잠깐 일어났는데 오히려 머리가 잘돌아감 
# ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

# M 은 OX 퀴즈 개수 
M = int(input())
# M 만큼 for 문을 타도록 
cnt_o = int(0)
for i in range(M) :
    # OX를 리스트로 만든다
    ox = input()
    li = list(ox)
    # o가 연속으로 있는지 rep 변수로확인. O일때 +1 , X일때 0으로 초기화
    rep =int(0)
    # o의 개수를 확인한다
    for m in range(0,len(li)) : #for m in range(0,len(li))
        print("rep은? " +str(rep)+" m은? " + str(m)+" cnt_o? " + str(cnt_o))
        if li[m] == str('X'):
            rep = 0
            m += 1
            print('X임')
            
        elif li[m] == str('O'):
            rep += 1
            cnt_o += 1*rep
            m += 1
            print(str(rep) + '연속 O임 // '+ str(rep))
    print (cnt_o)
    # 연속으로 있는 o는 연속 개수만큼 점수가 +1된다 (o = 1/ oo = 2 / ooo = 3)

#다른 사람 답
a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s: # 리스트에 직접 for문을 돌린다 
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)

#보완한 답(1) #for문에 list를 직접 넣는 방식
M = int(input())
for i in range(M) :
    ox = input()
    li = list(ox)
    rep = 0
    cnt_o = 0   
    for m in li :
        if m == 'O':
            rep += 1
            cnt_o += rep
        else :
            rep = 0
    print (cnt_o)

#보완한 답(1) # list 길이만큼 for문을 반복하고 직접 리스트 값 비교하는 방식
M = int(input())
for i in range(M) :
    ox = input()
    li = list(ox)
    rep = 0
    cnt_o = 0   
    for m in range(0,len(li)): 
        if li[m] == 'O' :
            rep += 1
            cnt_o += rep
        else :
            rep = 0
    print (cnt_o)