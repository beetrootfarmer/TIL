#X번째 분수를 구하시오 


# 1/1 (1)
# 1/2 ,2/1 (2~3)
# 3/1, 2/2, 1/3, (4~6)
# 1/4, 2/3, 3/2, 4/1, (7~10) m=4
# 5/1, 4/2, 3/3, 2/4, 1/5 (11~15)

x = int(input())
n = 0
m = 0
# while(n < x): # 한 줄의 가장 큰 숫자보다 입력값이 클때 반복문으로 몇번째 줄인지 알아내기 위함 
#     m += 1 #라인
#     n += m # 0 + 1, 1+2, 3+3, 6+4 반복되는 한 줄의 가장 큰 숫자 

# 라인이 넘어갈때 개수가 하나씩 늘어나는 구조에서 
# n라인의 가장 큰 숫자 = n라인의 개수 = (n(n+1))/2 .. 이 규칙을 이용해서 해결해보기
    # (n(n+1))/2 < 입력한 숫자  
    # (n(n+1)) < 입력한 숫자 * 2
while(True):
    m += 1
    n += m
    if ( m*(m+1) < 2*x ):
       continue
    else :
        break

g = n - x # 가장큰 숫자에서 입력값이 얼마의 차이가 있는지? 
if (m%2)==0: # 라인이 짝수일때 
    t = m - g # 분자는 라인 - 차이
    u = g + 1 # 분모는 차이 + 1
else : # 라인이 홀수일때 
    t = g + 1 # 분자는 차이 + 1
    u = m - g # 분모는 라인 - 차이
print(f'{t}/{u}')






# #다른사람답
# input_num = int(input())

# line = 0  # 사선 라인
# max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
# while input_num > max_num:
#     line += 1  
#     max_num += line  

# gap = max_num - input_num 
# if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
#     top = line - gap  #분자
#     under = gap + 1  #분모
# else :  # 사선 라인이 홀수번째 일 때
#     top = gap + 1  #분자
#     under = line - gap  #분모
# print(f'{top}/{under}')