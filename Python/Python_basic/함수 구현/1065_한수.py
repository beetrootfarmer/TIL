# 등차수열 : 연속된 두 개의 수의 차이가 일정한 수열
# 한수 : 정수 X의 각 자리가 등차수열을 이루는 수
    # 1자리, 2자리수는 모두 한수
    # 567, 246 같은 3자리 수 한수를 구해야한다 
# 1 <= N <= 1000 인 한수의 개수를 출력하는 프로그램

N = int(input())

def findhan(max):
    han = 0 # 한수의 개수
    k = 0
    for t in range(100,max):
        a = list()
        while ( t > 0 ) : # 123을 넣었을 때
            a.append(t % 10) # a[0]에 3이 담김
            t //= 10 # t에 12가 들어감 
            #!!!!!!!파이썬에서 /=는 나눈 값 그대로 들어감 //=이게 몫만 들어감
            k += 1 #a[1]에 t의 1의 자리수가 들어감
        # 배열 a[0] a[1] a[2]를 비교하는 함수
        if(a[0] - a[1] == a[1] - a[2]) :
            han += 1
    return han
    


# 한자리씩 분해해서 배열로 담는 함수
if N == 1000 :
    max = 1000
    print( findhan(max)+99)
elif N < 100 :
     print(N)
else :
    max = N+1
    print( findhan(max)+99) #1~99를 더해준다

