import io
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass

obj = Solution()
'''
data = obj.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
'''
data = obj.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(data)