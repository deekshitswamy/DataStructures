import io
from operator import mul
from functools import reduce
from typing import Counter, List
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        def dp(num):
            dp0,dp1=dp(num-k) if num-k in count else (1,0)
            return dp0+dp1, dp0*(pow(2,count[num])-1)
        return reduce(mul,(sum(dp(num)) for num in count if not count[num+k]  ))-1

obj = Solution()
#data = obj.beautifulSubsets(nums = [2,4,6], k = 2)
data = obj.beautifulSubsets(nums = [1], k = 1)
print(data)