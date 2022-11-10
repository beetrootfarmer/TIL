five = list(map(int, input().split()))
result = 0
for i in range(5):
    result += five[i]**2
print(result%10)