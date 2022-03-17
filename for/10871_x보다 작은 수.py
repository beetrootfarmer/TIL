# N은 입력할 정수 개수, X는 기준 정수. X보다 작은 수를 출력
N, X = map(int, input().split())
a = list(map(int, input().split()))
for i in range(N) :
    if (a[i] < X) :
        print(a[i], end=' ')#end : 기본값은 줄바꿈인데 , 지정 문자로 마치기
                            #sep : 리스트 구분 기본값은 쉽표, 지정문자를 사용해서 요소를 구분
