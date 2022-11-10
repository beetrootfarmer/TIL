N = int(input())
sangguen = list(map(int, input().split()))
M = int(input())
data = list(map(int, input().split()))
for i in range(M):
    print(sangguen.count(data[i]), end=' ')
print()