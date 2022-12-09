def fibo(n):
	if n <= 2:
		return n
	sm, v1, v2 = 0, 1, 2
	
	for i in range(2, n):
		sm = (v1 + v2) % 15746
		v1 = v2
		v2 = sm
	return sm

print(fibo(int(input())))