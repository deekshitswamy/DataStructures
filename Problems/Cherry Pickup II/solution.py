import io
from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @lru_cache(None)
        def dp(i,j,k):
            if not 0<=j<=k<n:
                return -inf
            if i==m:
                return 0
            ans=grid[i][j]+(j!=k)*grid[i][k]
            return ans+max(dp(i+1,y,z) for y in (j-1,j,j+1) for z in (k-1,k,k+1))
        return dp(0,0,n-1)

obj = Solution()
#data = obj.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
data = obj.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])
print(data)