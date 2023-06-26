# 양방향 순환 큐
# 여기서 잠깐
# queue는 LILO을 지원하는 친구
# deque는 stack과 queue의 기능을 모두 가진 친구
# 그리고 queue, list보다 deque가 훨씬 빠르다@
from collections import deque

# 1. 첫번째 원소 출력
# 2. 왼쪽으로 한칸 이동(첫번째 원소가 가장 뒤로)
# 3. 오른쪽으로 한칸 이동(마지막 원소가 가장 앞으로)

# 접근 : 현재위치를 파악하고 2와 3의 탐색경우를 각각 확인 후 더 적은 이동 횟수인 곳으로 현재위치를 이동

N, M = map(int, input().split())

jm = list(map(int, input().split()))    # 지민이가 뽑는 숫자 리스트
q = deque(list(range(1,N+1)))           # 1~N 숫자 큐
now = 0                                 # 현재위치 인덱스번호
answer = 0                              # 총 연산 횟수

# 1) jm을 순서대로 탐색한다
for j in jm:

    if j == q[now]:
        q.popleft()
    else:
        r, l = 0,0
        temp = now
        while j != q[now] and r < N:
            if now < N-1:
                now += 1
                r += 1
            else:
                now = 0
        now = temp
        while j != q[now] and l < N:
            if now > 0:
                now -= 1
                l += 1
            else:
                now = len(q)-1
                l += 1
        now = 0
        if r < l:                       # 2번 연산
            for i in range(r):
                a = q.popleft()
                if a == j: break
                q.append(a)

            answer += r
        else:                           # 3번 연산
            for i in range(l+1):
                a = q.pop()
                if a == j: break
                q.appendleft(a)
            answer += l
        if q[now] == j: q.popleft()

print(answer)

# 2) 현재 위치에서 2,3을 각각 탐색한다
# 3) 더 적은 이동횟수의 방향으로 현재 위치를 이동한다

