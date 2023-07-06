import io
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_range  = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sum_range  += nums[right]

            while sum_range  >= target:
                res = min(res, right - left + 1)
                sum_range  -= nums[left]
                left += 1

        return res if res != float('inf') else 0
obj = Solution()
#data = obj.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
#data = obj.minSubArrayLen(target = 4, nums = [1,4,4])
data = obj.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])
print(data)