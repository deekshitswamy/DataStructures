import io
from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            curmax=0
            for x in range(1,min(k,i)+1):
                curmax=max(curmax,arr[i-x])
                dp[i]=max(dp[i],dp[i-x]+curmax*x)
        return dp[n]

obj = Solution()
#data = obj.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)
#data = obj.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4)
data = obj.maxSumAfterPartitioning(arr = [1], k = 1)
print(data)