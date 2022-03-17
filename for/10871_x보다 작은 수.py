# N은 입력할 정수 개수, X는 기준 정수. X보다 작은 수를 출력
N, X = map(int, input().split())
a = list(map(int, input().split()))
for i in range(N-1) :
    if ((X-1) < a[i]) :
        del a[i]
print(*a, sep=' ')#sep : 지정문자를 사용해서 요소를 구분
