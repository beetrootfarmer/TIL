N = int(input())

for i in range(1,N+1) :
    star = str('*')
    space = str(' ')
    spacei = int(N-i)
    print((space*spacei)+(star*i))
   
