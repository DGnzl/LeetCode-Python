from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hor = set()
        vert = set()
        h, v = 0,0
        # Print matrix
        print("Before")
        for x in matrix:
            print(x)
        for x in matrix:
            v = 0
            for y in x:
                if y == 0:
                    hor.add(h)
                    vert.add(v)
                v += 1
            h += 1
        for x in hor:
            for y in range(len(matrix[x])):
                matrix[x][y] = 0
        for x in vert:
            for y in range(len(matrix)):
                matrix[y][x] = 0
        print("\nAfter:")
        for x in matrix:
            print(x)
# Medium
# Sets
    def setZeroes2(self, matrix):
        row, column = len(matrix), len(matrix[0])
        hor, vert = set(), set()
        # Iterate through all the elements
        for x in range(row):
            for y in range(column):
                # If 0 is found, record the x and y in the set
                if matrix[x][y] == 0:
                    hor.add(x)
                    vert.add(y)
        # Iterate through all the elements again
        for x in range(row):
            for y in range(column):
                    # If the current element is in either set then set it equal to 0
                    if x in hor or y in vert:
                        matrix[x][y] = 0

Solution.setZeroes2(Solution, [[1,1,1],[1,0,1],[1,1,1]])
Solution.setZeroes2(Solution, [[0,1,2,0],[3,4,5,2],[1,3,1,5]])