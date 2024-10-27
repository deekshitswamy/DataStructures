import io
from typing import List
class Solution:
    def window(self, size, rows, cols, matrix):
        total_ones = 0
        for row_index in range(rows - size + 1):
            for col_index in range(cols - size + 1):
                all_ones = True
                for i in range(size):
                    for j in range(size):
                        if matrix[row_index + i][col_index + j] != 1:
                            all_ones = False
                            break
                    if not all_ones:
                        break
                if all_ones:
                    total_ones += 1
        return total_ones

    def countSquares(self, matrix: List[List[int]]) -> int:
        total = 0
        rows = len(matrix)
        cols = len(matrix[0])

        for size in range(1, min(rows, cols) + 1):
            total += self.window(size, rows, cols, matrix)
        
        return total

obj = Solution()
'''
data = obj.countSquares(matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])
'''
data = obj.countSquares(matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
])
print(data)