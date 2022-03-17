# sys.stdin.readline() 
# 문자열로 받음 , 형변환 필요 
import sys  #파이썬 인터프리터가 제공하는, 변수와 함수를 제어할 수 있게해주는 모듈

T = int(input()) #테스트 케이스
for i in range(T) :
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)