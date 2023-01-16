import sys
# H높이의 K개업무를 R일동안 진행하는데
# 결제 처리가 완료된 일의 합을 구하시오

# 홀수번째 날 = L에서 받은 일
# 짝수번째 날 = R에서 받은 일

# 1일에 말단 진행 -> 상사 처리 -> 부사장 처리 시 result에 저장

input = sys.stdin.readline
h, k, r = map(int, input().split())
ants = 2**h # 말단노드의 개수
tasks = []
for i in range(ants):
    tasks.append(list(map(int, input().split())))
for i in range(r) : #r 일 동안
