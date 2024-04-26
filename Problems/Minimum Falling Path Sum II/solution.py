import io
from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[0]
        for r in range(1,n):
            nxt = [float("inf")] * n
            for curr in range(n):
                for prev in range(n):
                    if prev != curr:
                        nxt[curr] = min(nxt[curr],grid[r][curr]+dp[prev])
            dp = nxt
        return min(dp)

obj = Solution()
#data = obj.minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]])
data = obj.minFallingPathSum(grid = [[7]])
print(data)