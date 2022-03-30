m = int(input())
n = int(input())

mn = [0 for i in range(n-m+1)] 
c=0

for i in range(m,n+1):
    for n in range(2,i):
        if i % n == 0:
            mn[c] = 'x'
            break
    if mn[c] != 'x':
        mn[c] = i
    c+=1

while('x' in mn):
    mn.remove('x')

if 1 in mn:
    mn.remove(1)
if sum(mn) >0:
    print(sum(mn))
    print(mn[0])
else:
    print(-1)

# 위 방식 : 0을 넣은 배열을 만들어줘서 조건 검사 후 x 혹은 숫자 값을 넣어주고 0 없애는 개 복잡한 방식
#=================================세 가지 방식 맞음===========================호호호============================
# 아래 방식 : 빈 배열 만들어서 조건 검사 후 0 혹은 숫자값을 넣고 0없앤다

m = int(input())
n = int(input())

mn = []

for i in range(m,n+1):
    c=0
    for n in range(2,i):
        if i % n == 0:
            mn.append(0)
            c = 1
            break
    if c != 1:
        mn.append(i)

if 1 in mn:
    mn.remove(1)
while( 0 in mn):
    mn.remove(0)

if sum(mn) >0:
    print(sum(mn))
    print(min(mn))
else:
    print(-1)

#============================================================호호호============================
# 아래 방식 : 빈 배열 만들어서 조건 검사 후 숫자값을 넣는다. 제일 간단한 방식!!

m = int(input())
n = int(input())

mn = []
for i in range(m,n+1):
    e = 0
    if i > 1 : #1은 소수가 아니기 때문에 제외하고 만들어줘야함 
        for n in range(2,i):
            if i % n == 0:
                e += 1
                break
        if e == 0:
            mn.append(i) 
if sum(mn)>0:
    print(sum(mn))
    print(min(mn))
else :
    print(-1)
