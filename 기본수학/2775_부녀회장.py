case = int(input())
for i in range(case):
    fl = int(input()) #1
    ho = int(input()) #3
    count=0
    for i in range(fl):
        for i in range(1,ho+1):
            count += i
    print(count) #6

# “a층의 b호에 살려면 자신의 아래(a-1)층의 
# 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 
# 1층의 3호에 살려면 자신의 아래(0층)의
# 1호부터 3호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다

# 0층 [1,2,3,4,5,6 ...]
# 1층 []