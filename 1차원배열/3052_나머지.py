#숫자 10개를 받고 42로 나누었을때 나머지값이 다른 것 갯수구하기
#42의 배수로만 이뤄져있을 때 출력값은 1(모두 공통된 나머지값)

res=[]
for i in range(0,10):
    m = int(input())
    #print(m%42)
    res.append(int(m % 42))
    #print(res[i])
# set() 리스트의 중복요소 제거
res = set(res)
res = list(res)
print(len(res))

    