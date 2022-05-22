import sys

n = int(sys.stdin.readline())
a = []
while (n % 10) > 0:
	a.append(n%10)
	n = n // 10
a.sort()
a.reverse()
for i in a:
	print(i, end='')