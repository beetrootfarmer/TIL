#ljes=njak = lj e š nj a k (6개의 크로티아 알파벳으로 이루어져있음)
#입력된 문자열이 몇개의 크로티아 알파벳으로 이루어져있는지 ?
#replace 로 지정 문자열 치환 삭제
s = ['c=','c-','dz=','d-','lj','nj','s=','z=']
w = input()
c =0
for i in s:
    c += w.count(i)
    w = w.replace(i," ")
w = w.replace(" ","")
print(len(list(w))+c)