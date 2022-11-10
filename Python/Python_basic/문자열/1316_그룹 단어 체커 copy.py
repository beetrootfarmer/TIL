N = int(input())
g = 0
for i in range(N):
    st = input()
    for i in range(0,len(st)-1):
        s = list(st)
        if s[i] == s[i+1] :
           st = st.replace(s[i],' ')
    st = st.replace(' ','')
    s = ''.join(dict.fromkeys(st))

    if s == st :
        g += 1
    else : 
        g += 0
print(g)
   
