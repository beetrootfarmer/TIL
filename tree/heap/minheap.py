N = 6
data = [3, 6, 9, 1, 8, 2]

# tree = 리스트로 표현
# 0번 인덱스는 사용하지 않는다
tree = [0 for _ in range(N+1)]
last = 1
for i in range(len(data)):
    if not tree[i]:
        tree[last] = data[i]
    else:
        last += 1
        child = last
        parent = child // 2

        tree[child] = data[i]

        while parent and tree[parent] > tree[child]:
            tree[parent], tree[child] = tree[child] , tree[parent]
            child = parent
            parent = child // 2 # parent = parent//2

print(tree)
