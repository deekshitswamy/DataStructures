import io
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            if i>=n or j>=m or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            ans=dfs(i,j+1)
            ans+=dfs(i+1,j)
            ans+=dfs(i,j-1)
            ans+=dfs(i-1,j)
            return ans
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return dfs(i,j)

obj = Solution()
#data = obj.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
#data = obj.islandPerimeter(grid = [[1]])
data = obj.islandPerimeter(grid = [[1,0]])
print(data)