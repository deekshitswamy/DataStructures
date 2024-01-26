import io
from typing import List
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        
        def rec(r,c,M):
            if r<0 or c<0 or r>=m or c>=n:
                return 1
            if M==0:
                return 0
            ans=0
            for d in directions:
                new_r=r+d[0]
                new_c=c+d[1]
                ans+=rec(new_r,new_c,M-1)
            return ans
        directions=[(1,0),(-1,0),(0,1),(0,-1)]    
        return rec(startRow,startColumn,maxMove)%(10**9+7)

obj = Solution()
#data = obj.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0)
data = obj.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1)
print(data)
