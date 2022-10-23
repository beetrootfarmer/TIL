case = int(input())
for i in range(case):
    fl = int(input()) 
    ho = int(input()) 
    floor = [[0]*(ho) for i in range(0,fl+1)]
    
    for i in range(0,ho):
        floor[0][i] = i+1
    
    for i in range(1,fl+1):
        for d in range(0,ho):
            for m in range(0,d+1):
                floor[i][d] += floor[i-1][m]
    print(floor[fl][ho-1])

#2차원 배열
# 1행 : list[0] 
# 2열 : list[:,1]
# 2열 1~3원소 : list[:2,1]
# 2열 3~마지막 원소 : list[2:,1]
# 조건부 접근
# 2보다 큰 원소 : list[x > 2]
# 원소 수정
# 2행 3열의 원소를 100으로 : list[1,2]=100

# “a층의 b호에 살려면 자신의 아래(a-1)층의 
# 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 
# 1층의 3호에 살려면 자신의 아래(0층)의
# 1호부터 3호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다

# 0층 [1,2,3,4,5,6 ...]
# 1층 [1,3,6,10,15,21 ...]
# 2층 [1,4,10,20,35,56 ...]