import io
from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        for j in range(m):
            col=sum(grid[i][j]==grid[i][0] for i in range(n))
            ans+=max(col,n-col)*2**(m-1-j)
        return ans

obj = Solution()
#data = obj.matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]])
data = obj.matrixScore(grid = [[0]])
print(data)