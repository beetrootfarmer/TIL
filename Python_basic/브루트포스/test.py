global v
v = 10

def f():
    # global v
    v = 100
    print(v)
    print(locals())
f()
print(v)
name resolution은 로컬스코프, 인클로징 스코프, 글로벌 스코프, 빌트인 스코프 순서대로 탐색을 한다.
global v
v = 10

def f():
v = 100
print(v)
print(locals())

f()
print(v)
 
위에서 선언한 변수 v는 전역변수로 마지막 줄의 print에서 출력되는 것을 볼 수 있다. 그런데 f() 함수 내부의 v는 지역변수로 내부에서 선언된 100이 출력되고 locals()을 출력했을 때도  v:'100'으로 출력되는 것을 확인할 수 있다. 