num = []

for i in range(2, 246913):
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        num.append(i)

while True:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in num:
        if n < i <= 2*n:
            res += 1

    print(res)

# ===============예진답===============
import math

lim=123456

def count_primeNum(n):
  for i in range(2,int(math.sqrt(n))+1):
      if n%i==0:
        return False
  return True # 소수이면 트루

n=list()
m=list()
while True:
  x=int(input())
  if x==0:
    break
  n.append(x)
m.append(False)
m.append(False)

for i in range(2,2*lim+1):
  m.append(count_primeNum(i))
      
for j in range(len(n)):
  count=0
  for i in range(n[j]+1,2*n[j]+1):
    if m[i]== True:
      count+=1

  print(count)
