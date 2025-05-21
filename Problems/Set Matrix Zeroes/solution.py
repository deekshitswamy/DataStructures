import io
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        found_position = None
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    found_position = (i, j)
                    arr.append(found_position)

        def setzero(arr, matrix):
            for pos in arr:
                row, col = pos
                for j in range(len(matrix[0])):
                    matrix[row][j] = 0
                for i in range(len(matrix)):
                    matrix[i][col] = 0

        setzero(arr, matrix)

obj = Solution()
#data = obj.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])
data = obj.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
print(data)