'''
463 岛屿的周长
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
'''
# 我的代码
# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
grid = [[1], [1]]
m = 0
n = 0
o = 0
for i in range(len(grid)):
    m += grid[i].count(1)
    for j in range(len(grid[i]) - 1):
        if len(grid[i]) == 1:
            n = 0
        elif grid[i][j] == 1 and grid[i][j+1] == 1:
            n += 1
for i in range(len(grid[0])):
    for j in range(len(grid) - 1):
        if len(grid[0]) == 1:
            if grid[j][i] == 1 and grid[j+1][i] == 1:
                o += 1
        elif len(grid[0]) > 1:
            if grid[j][i] == 1 and grid[j+1][i] == 1:
                o += 1
p = 4*m - 2*n - 2*o
print(p)


# 最优化代码
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return 0
#         m, n = len(grid), len(grid[0])
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     down = 2 if i < m - 1 and grid[i + 1][j] == 1 else 0
#                     right = 2 if j < n - 1 and grid[i][j + 1] == 1 else 0
#                     ans += 4 - down - right
#         return ans
