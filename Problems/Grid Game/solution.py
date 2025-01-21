import io
from typing import List
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        suffix, prefix, ans = sum(grid[0]), 0, inf
        for n1, n2 in zip(*grid):
            suffix -= n1
            ans = min(max(suffix, prefix), ans)
            prefix += n2
        return ans

obj = Solution()
#data = obj.gridGame(grid = [[2,5,4],[1,5,1]])
#data = obj.gridGame(grid = [[3,3,1],[8,5,2]])
data = obj.gridGame(grid = [[1,3,1,15],[1,3,3,1]])
print(data)