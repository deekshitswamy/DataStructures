import io
from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        location_map = [None] * (rows * cols + 1)

        for i in range(rows):
            for j in range(cols):
                location_map[mat[i][j]] = (i, j)

        row_map = [cols] * rows
        col_map = [rows] * cols
        
        for idx, val in enumerate(arr):
            i, j = location_map[val]
            row_map[i] -= 1
            col_map[j] -= 1

            if row_map[i] == 0 or col_map[j] == 0:
                return idx

obj = Solution()
#data = obj.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]])
data = obj.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]])
print(data)