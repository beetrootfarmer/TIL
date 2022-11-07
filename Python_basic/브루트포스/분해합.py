
def count_len(n):
    len = 1
    while (n // 10) > 0:
        n = n // 10
        len += 1
    return len

n = int(input())
t = 0
for i in range(1, n + 1):
    t += 1
    sum = t
    tstr = str(t)
    for i in range(0,len(tstr)):
        sum += int(tstr[i])
    if (sum == n):
        print(t)
        break
    if (t == n):
        print(0) 