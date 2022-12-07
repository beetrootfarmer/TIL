import sys
input = sys.stdin.readline

N = int(input())    # 참가자 N명
                    # 참가자가 1명 남을때까지 t**3 배수로 참가자를 제거한다
                    # 시계방향으로 회전하면서 제거
                    # N-1번 반복하면서 제거
t = 1
next = 0
students = list(range(1,N+1))       # 1~N까지의 숫자가 담긴 학생 배열
for _ in range(1,N):                # 학생이 한 명 남을 때 까지 반복

    ls = len(students)              # 학생 배열의 길이를 저장할 변수 ls
    count = t**3                    # 몇번 카운팅 해야할지 저장할 변수 count
    if (count + next-1) >= ls:      # count + next - 1 ==> 제거할 다음 학생 총 카운트 - 1(인덱스)
        a = (count + next-1)%ls     # ls의 길이로 나눈 나머지를 인덱스로 사용해 학생 배열에서 Pop
        students.pop(a)
    else:
        a = count + next-1          # ls보다 작은 수라면 a인덱스를 pop
        students.pop(a)
    next = a                        # 다음 시작할 위치는 next
    if next >= len(students):       # 만약 next가 학생 배열의 길이보다 크면
        next = next % len(students) # 나머지값으로 저장
    t+=1                            # 3제곱 할 수 t에 1을 더해줘서 다음단계로
print(students[0])                  # 마지막에 학생배열에 남은 수 하나를 출력