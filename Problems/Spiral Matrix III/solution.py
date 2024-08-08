import io
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans=[]
        dx,dy,n=0,1,0
        while len(ans)<rows*cols:
            for i in range(n//2+1):
                if 0<=rStart<rows and 0<=cStart<cols:
                    ans.append([rStart,cStart])
                rStart=rStart+dx
                cStart=cStart+dy
            dx,dy,n=dy,-dx,n+1
        return ans

obj = Solution()
#data = obj.spiralMatrixIII(rows = 1, cols = 4, rStart = 0, cStart = 0)
data = obj.spiralMatrixIII(rows = 5, cols = 6, rStart = 1, cStart = 4)
print(data)