from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        
        for x in range(rows):
            for y in range(columns):
                if x and y:
                    grid[x][y] += min(grid[x-1][y], grid[x][y-1])
                elif x:
                    grid[x][y] += grid[x-1][y]
                elif y:
                    grid[x][y] += grid[x][y-1]
        
        return grid[-1][-1]

print(Solution.minPathSum(Solution, [[1,2,3],[4,5,6]])) # 12
print(Solution.minPathSum(Solution, [[1,3,1],[1,5,1],[4,2,1]])) # 7
