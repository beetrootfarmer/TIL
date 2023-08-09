# 숫자 N을 입력받고 1로 만들 수 있는 연산 횟수의 최솟값을 리턴
# -1, %2, %3 3가지의 연산을 사용할 수 있어서
# a, 3*N 길이의 2차원 배열을 만들고
# b. 1부터 시작해서 세가지를 적용하고 배열에 저장한다.
# c. 1에서 계산한 값의 인덱스로 이동해서 cnt를 늘리며 반복한다(재귀함수)
# d. N이 나오면 종료한다
# e. cnt를 리턴한

N = int(input())
cnt = N # 최대 N은 1에서부터 반복적으로 1을 더한 값
def recursion(x, c):
    global N, cnt

    if x > N or c > cnt:
        return

    # 저장하거나 검색할 숫자 x가 N이 나올때까지 cnt 를 늘리며 반복한다
    if x == N and c < cnt:
        cnt = c
        return

    recursion(x+1, c+1)
    recursion(x*2, c+1)
    recursion(x*3, c+1)

recursion(1, 0)
print(cnt)