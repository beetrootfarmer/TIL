m = int(input())
n = int(input())
gap = n-m+1 #100 - 60 = 40
mn = [0 for i in range(gap)] # range 들어간 숫자 길이의 배열에 0을 넣어 생성

print("initial mn의 길이 ===", len(mn))
for i in range(0,gap):
    mn[i] = m
    m += 1
mn.remove(77)
print("after mn의 길이==",len(mn))
print("after mn==",mn)

