import io
from typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        adj = [[1]*n*3 for _ in range(n*3)]
        for i in range(n):
            for j in range(n):
                r = i*3
                c = j*3
                if grid[i][j]=="/":
                    adj[r+2][c] = 0
                    adj[r+1][c+1] = 0
                    adj[r][c+2] = 0
                elif grid[i][j]=="\\":
                    adj[r][c] = 0
                    adj[r+1][c+1] = 0
                    adj[r+2][c+2] = 0
   
        count = 0
        for i in range(n*3):
            for j in range(n*3):
                if adj[i][j] == 1:
                    self.dfs(adj, i, j)
                    count+=1
        

        return count


    def dfs(self, adj: List[str], i: int, j:int) -> int:
        size = len(adj)
        adj[i][j] = 0
        dir = [[-1,0],[0,-1],[0,1],[1,0]]
        for dx, dy in dir:
            x, y = i + dx, j + dy 

            if(x<0 or x>=size or y<0 or y>=size or adj[x][y]==0):
                continue
            
            self.dfs(adj, x, y)

obj = Solution()
#data = obj.regionsBySlashes(grid = [" /","/ "])
#data = obj.regionsBySlashes(grid = [" /","  "])
data = obj.regionsBySlashes(grid = ["/\\","\\/"])
print(data)