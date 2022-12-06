import sys
input = sys.stdin.readline

N = int(input())    # 참가자 N명
                    # 참가자가 1명 남을때까지 t**3 배수로 참가자를 제거한다
                    # 시계방향으로 회전하면서 제거
                    # N-1번 반복하면서 제거
t = 1
next = 0
students = list(range(1,N+1))
print(students)
for _ in range(1,N):

    ls = len(students)

    count = t**3
    if count > ls:
        count = count % ls # 시작점 기준으로 몇번째 사람이 제거되는지 배열의 길이 미만으로 만듦

    if (count + next-1) >= ls:
        a = students.pop((count + next-1)%ls)
    else:
        a = students.pop(count + next-1)
    print('a', a)
    print('next', next, 'count', count)
    print('students', students)
    next += count-1
    # if next >= len(students):
    #     next = next % len(students)
    # if next + count > len(students):


    # next = count-1      # 한명이 빠지면 그 다음사람부터 시작

    t+=1
