# 2D 지도를 받고 해당 지도의 섬 갯수를 리턴하라
# 1. 지도 전체를 순회한다
# 2, 1이 나왔을 때 DFS를 사용해 방문처리를 한다
# 3. DFS를 호출한 횟수를 리턴한다

def numIslands(grid):
    row, col = len(grid), len(grid[0])
    island = 0

    def DFS(i,j, row,col):
        if grid[i][j] == '0':
            return
        for m in [(1,0),(0,1),(-1,0),(0,-1)]:
            ii, jj = i + m[0], j + m[1]
            if 0<=ii<row and 0<=jj<col and grid[ii][jj] == '1':
                grid[ii][jj] = '-1'
                DFS(ii,jj, row, col)
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                grid[i][j] = '-1'
                island += 1
                DFS(i, j, row,col)
    return island

a = numIslands(
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
)
print(a)