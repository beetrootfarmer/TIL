# 테스트 케이스 T
#입력한 T 만큼의 횟수로 input을 받아서 두 수를 더하는 for문 돌리기
T = int(input())
for i in range(T) :#T만큼 반복
    a,b = map(int,input().split())
    print(a+b)
