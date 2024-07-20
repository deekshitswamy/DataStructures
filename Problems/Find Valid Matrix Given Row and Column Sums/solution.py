import io
from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c=len(rowSum), len(colSum)
        arr=[[0]*c for _ in range(r)]
        i, j=0, 0
        while i<r and j<c:
            x=min(rowSum[i], colSum[j])
            arr[i][j]=x
            rowSum[i]-=x
            colSum[j]-=x
            i+=(rowSum[i]==0)
            j+=(colSum[j]==0)
        return arr

obj = Solution()
#data = obj.restoreMatrix(rowSum = [3,8], colSum = [4,7])
data = obj.restoreMatrix(rowSum = [5,7,10], colSum = [8,6,8])
print(data)