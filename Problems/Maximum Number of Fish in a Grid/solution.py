import io
from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        path=[(0,1),(1,0),(0,-1),(-1,0)]
        n=len(grid)
        m=len(grid[0])
        def dfs(row,col):
            c[0]+=grid[row][col]
            grid[row][col]=0
            for i,j in path:
                new_row=i+row
                new_col=j+col
                if 0<=new_row<n and 0<=new_col<m and grid[new_row][new_col]!=0:
                    dfs(new_row,new_col)
        maxi=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    c=[0]
                    dfs(i,j)
                    maxi=max(maxi,c[0])
            
        return maxi

obj = Solution()
#data = obj.findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]])
data = obj.findMaxFish(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])
print(data)