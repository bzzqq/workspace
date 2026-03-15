grid = [[1,2,4],[3,3,1]]
MaxValue = 0
a = []
for row in grid:
    row.sort()
print(grid)
for i in range(grid[0]):
    for j in range(grid):
        a.append(grid[j][i])
   
print(MaxValue)
