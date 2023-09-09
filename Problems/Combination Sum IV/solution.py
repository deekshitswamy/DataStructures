import io
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for t in range(target+1):
            for num in nums:
                if num<=t:
                    dp[t]+=dp[t-num]

        return dp[target]

obj = Solution()
#data = obj.combinationSum4(nums = [1,2,3], target = 4)
data = obj.combinationSum4(nums = [9], target = 3)
print(data)