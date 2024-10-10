import io
from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        dec = [0]

        # Decreasing stack
        for i in range(1, len(nums)):
            if nums[i] < nums[dec[-1]]:
                dec.append(i)

        max_ramp = 0

        # Loop from right to left
        for i in range(len(nums) - 1, -1, -1):
            while dec and nums[i] >= nums[dec[-1]]:
                max_ramp = max(max_ramp, i - dec.pop())

        return max_ramp

obj = Solution()
#data = obj.maxWidthRamp(nums = [6,0,8,2,1,5])
data = obj.maxWidthRamp(nums = [9,8,1,0,1,9,4,0,4,1])
print(data)