import io
from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0

        for num in nums:
            current_max = max(0, current_max + num)
            max_sum = max(max_sum, current_max)
            current_min = min(0, current_min + num)
            min_sum = min(min_sum, current_min)

        return max(abs(max_sum), abs(min_sum))

obj = Solution()
#data = obj.maxAbsoluteSum(nums = [1,-3,2,3,-4])
data = obj.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2])
print(data)