H, M = map(int, input().split())

#분이 45분 미만일 때 
if(M < 45) and (0<H<25) : print((H-1), (M+15))
elif(M < 45) and (H == 0) : print(23, (M+15))
#분이 45분~59분일때 
elif (45 <= M < 60) : print(H, M-45)
else : ("0~24사이의 시간과 0~60사이의 분을 입력하세요")