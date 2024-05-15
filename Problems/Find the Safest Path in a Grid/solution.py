import io
from typing import List
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        pass

obj = Solution()
#data = obj.maximumSafenessFactor(grid = [[1,0,0],[0,0,0],[0,0,1]])
#data = obj.maximumSafenessFactor(grid = [[0,0,1],[0,0,0],[0,0,0]])
data = obj.maximumSafenessFactor(grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
print(data)