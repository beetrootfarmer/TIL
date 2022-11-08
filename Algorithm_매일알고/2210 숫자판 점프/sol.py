import sys
sys.stdin = open('input.txt')

def dfs(i, j, num):
    if len(num) == 6:
        if num not in results:
            results.append(num)
        return

    for m in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ii, jj = i+m[0], j+m[1]
        if 0<= ii < 5 and 0<= jj < 5:
            dfs(ii, jj, num + nums[ii][jj])

# 5 * 5 숫자판
nums = [list(input().split(sep=' ')) for _ in range(5)]
results = []
for i in range(5):
    for j in range(5):
        dfs(i, j, nums[i][j])
print(len(results))