# 자연수 세 자리의 곱에서 과정 숫자 구하기
A =int (input('A : 세자리 숫자를 입력해주세요'))
B =int (input('B : 세자리 숫자를 입력해주세요'))
# 배열을 사용하는 방법
# B의 숫자를 하나씩 꺼내기
a = []
for i in str(B): a.append(i)
#하나씩 곱하기
b1 = a[0]
print(A * int(b1))
b2 = a[1]
print(A * int(b2))
b3 = a[2]
print(A * int(b3))
print(A*B)

# 위의 방법은 터미널에서는 되는데 백준에서 안된다
# 숫자를 하나씩 쪼개서 곱하는방법, 훨씬 짧다
A =int (input('A : 세자리 숫자를 입력해주세요'))
B = input('B : 세자리 숫자를 입력해주세요')
for i in map(int, str(B)) : print(i * A) 
print(A*int(B))

# 또..? 위의 방법은 터미널에서는 되는데 백준에서 안된다
# 나머지로 두번째 숫자 1의자리 10의자리 100의자리 구하기
A =int(input('A : 세자리 숫자를 입력해주세요'))
B =int(input('B : 세자리 숫자를 입력해주세요'))
print(A*(B%10)) #세번째 숫자
print(A*((B%100)//10)) #두번째 숫자 .. 나누기 / 아니고 //
print(A *(B//100))#세번째숫자
print(A*B)