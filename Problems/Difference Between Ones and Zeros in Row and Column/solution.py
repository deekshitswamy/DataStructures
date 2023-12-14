import io
from typing import List
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        m, n = len(grid), len(grid[0])
        for row in grid:
            d = 2*sum(row) - m
            diff.append([d for n in row])

        for i, col in enumerate(zip(*grid)):
            d = 2*sum(col) - n
            for row in diff:
                row[i] += d
        return diff

obj = Solution()
#data = obj.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]])
data = obj.onesMinusZeros(grid = [[1,1,1],[1,1,1]])
print(data)