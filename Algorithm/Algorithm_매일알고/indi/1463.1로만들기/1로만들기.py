# 숫자 N을 입력받고 1로 만들 수 있는 연산 횟수의 최솟값을 리턴
# -1, %2, %3 3가지의 연산을 사용할 수 있어서 거꾸로 함
N = int(input())
arr = [N+1]*(N+1)
arr[1] = 0

def update(i, idx):
    if i <= N:
        if arr[i] != (N+1):
            arr[i] = min(arr[i], arr[idx] + 1)
        else:
            arr[i] = arr[idx] + 1
# 1~N만큼 반복하면서 해당 숫자를 만들 수 있는 최소 횟수를 저장
for i in range(1, N):
    for x in (i+1, i*2, i*3):
        update(x, i)

print(arr[N])