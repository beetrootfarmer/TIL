# 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내시오~

w = list(input().lower())

from string import ascii_lowercase
asc  = list(ascii_lowercase)

m = 0
for i in asc:
    if i in w:
        if m < w.count(i) : 
            l = i
            m = w.count(i)
        elif m == w.count(i):
            l =('?')
print(l.upper())