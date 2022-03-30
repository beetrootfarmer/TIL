# #설탕배달
# #최대한 적은 봉지 
#다시
N = int(input())
m = N//5 #몫
rest = N%5 #나머지
m3 = N//3 #몫3
rest3 = N%3 #나머지3

#5로 나눠질 때 
answer = -1
if rest==0 :  
    answer = m
elif N>9:
    for i in range(1,5):
        m=(N-(3*i))//5  
        rest =(N-(3*i))%5  
        if rest == 0:
            answer = i+m
            break
elif N<10:
    if rest3==0 and m3>0:
        answer = m3
    elif N == 8:
        answer = 2

print(answer)

# # 5로 나눈 나머지가 1일 때 => 5는 (몫 - 1) 이고 3은 2 => 21
# # 5로 나눈 나머지가 2일 때 => 5는 (몫 - 4) 이고 3은 4 => 22
# # 5로 나눈 나머지가 3일 때 => 5는 (몫) 이고 3은 1 => 23
# # 5로 나눈 나머지가 4일 때 => 5는 (몫 - 1) 이고 3은 3 => 24
# # 5로 나눈 나머지가 없을 때 => 5는 몫
# # 5로 나눠지지 않을 때 3으로 나눠서 나머지가 없으면 => 3은 몫
# # 5로 나눠지지 않을 때 3으로 나눠지지 않으면 => -1 출력 

# #다른사람 답
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)
