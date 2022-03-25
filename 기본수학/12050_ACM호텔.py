# 이건 어디가 틀렸게
# i를 int로 받아야지 for문에서 range(i)이렇게 쓸 수 있음 
i = input()
for i in i:
    H, W, N = map(int,input().split())
    ho = (N//H)+1
    fl = N % H
    if fl == 0 :
        ho = N//H
        fl = H
    print(f'{fl*100+ho}')
# [ f-string ]
# {}안에 변수 넣어서 스트링이랑 같이 출력하는 것 
# 이 답은 변수로 계산하는 값만 출력하기 때문에 f-string 안써도 맞음

#다른사람 답
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')

# VS Code에서는 출력되는데 틀린답이라는데
# 이유는 딱히 몰겓다
i = input()
for i in i:
    H, W, N = map(int,input().split())
    ho = int(N/H)
    fl = int(N%H) 
    if fl==0 :
        if ho < 10 : 
            ho ='0'+str(ho)
        print(str(H)+str(ho))
    else :
        if ho < 9 : 
            print(str(fl)+'0'+str(ho+1))
        else :
            print(str(fl)+str(ho+1))

   