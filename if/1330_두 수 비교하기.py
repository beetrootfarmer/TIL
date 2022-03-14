# < > ==
a, b = map(int,input().split())
if  a < b  : print("<")
elif a > b  : print(">")
else : print("==") 

#삼항 연산자
A,B = map(int,input().split())
print('>') if A > B else print('<') if A < B else print('==')