import io
from typing import List
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        s=set()
        ans=[0]
        def dfs(i,j,t):
            s.add((i,j))
            for k,l in (i-1,j),(i,j+1),(i+1,j),(i,j-1):
                if 0<=k<n and 0<=l<m and grid[k][l] and (k,l) not in s:
                    dfs(k,l,t+grid[k][l])
            ans[0],_=max(ans[0],t),s.remove((i,j))        
        for i,j in itertools.product(range(n),range(m)):
            if grid[i][j]:
                dfs(i,j,grid[i][j])
        return ans[0]

obj = Solution()
#data = obj.getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]])
data = obj.getMaximumGold(grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])
print(data)