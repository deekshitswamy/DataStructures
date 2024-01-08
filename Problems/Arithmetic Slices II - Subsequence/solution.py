import io
from typing import List
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        dp=[defaultdict(int) for _ in range (n)]
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                dp[i][diff]+=1+dp[j][diff]
                res+=dp[j][diff]

        return res

obj = Solution()
#data = obj.numberOfArithmeticSlices(nums = [2,4,6,8,10])
data = obj.numberOfArithmeticSlices(nums = [7,7,7,7,7])
print(data)