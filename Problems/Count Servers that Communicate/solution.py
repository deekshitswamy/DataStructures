import io
from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = [0]*m
        col = [0]*n
        for i in range(m):
            for j in range(n):
                row[i] += grid[i][j]
                col[j] += grid[i][j]

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i]>1 or col[j]>1):
                    total += 1

        return total

obj = Solution()
#data = obj.countServers(grid = [[1,0],[0,1]])
#data = obj.countServers(grid = [[1,0],[1,1]])
data = obj.countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])
print(data)