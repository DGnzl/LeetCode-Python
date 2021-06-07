from typing import List
# Medium
# Dynamic Programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the total number of rows and columns to iterate through
        rows, columns = len(grid), len(grid[0])
        
        for x in range(rows):
            for y in range(columns):
                # If x > 0 and y > 0
                # Check for the minimum of the element above or to the left
                # and add it to the current num
                if x and y:
                    grid[x][y] += min(grid[x-1][y], grid[x][y-1])
                # If x > 0 and y == 0
                # Add the number to the left to the current number
                elif x:
                    grid[x][y] += grid[x-1][y]
                # If x == 0 and y > 0
                # Add the number above the current number
                elif y:
                    grid[x][y] += grid[x][y-1]
        # Return the last number in the grid
        return grid[-1][-1]

print(Solution.minPathSum(Solution, [[1,2,3],[4,5,6]])) # 12
print(Solution.minPathSum(Solution, [[1,3,1],[1,5,1],[4,2,1]])) # 7
