#n = 카드의 개수
#m = 합에 근접한 수
#a = 카드의 수
n, m = map(int,input().split())
a = list(map(int,input().split()))

#m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합을 출력
#min = m에서 세 수를 더한 값을 뺀 것 
min = m
temp = 0
result = 0

for i in range(0, n - 2):
    for j in range (i + 1, n - 1):
        temp = m - (a[i] + a[j] + a[j + 1])
        if(temp < min and temp >= 0):
            min = temp
            result = a[i] + a[j] + a[j + 1]
print(result)
