# N개의 정수가 주어질 때 최소값과 최대값을 구하는 프로그램을 작성하시오 
N = int(input())
a = list(map(int,input().split()))

max = a[0]
min = a[0]
for i in range(0,N):
    if a[i] > max :
        max = a[i]
    if a[i] < min :
        min = a[i]
print(str(min)+' '+str(max))
