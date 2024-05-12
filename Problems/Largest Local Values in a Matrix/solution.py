import io
from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                ans[i][j]=grid[i][j]
                for di in range(3):
                    for dj in range(3):
                        ans[i][j]=max(ans[i][j],grid[i+di][j+dj])
        return ans

obj = Solution()
#data = obj.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
data = obj.largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])
print(data)