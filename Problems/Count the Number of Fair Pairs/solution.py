import io
from typing import List
from bisect import bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        ln = len(nums)
        
        def helper(l,target):
            r = ln - 1
            ans = 0
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    ans += r-l
                    l += 1
                else:
                    r -= 1
            return ans

        return helper(0,upper+1) - helper(0,lower)

obj = Solution()
#data = obj.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)
data = obj.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11)
print(data)