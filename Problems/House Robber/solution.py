import io
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        nonAdjacent = nums[0]
        adjacent = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            curr = max(nums[i] + nonAdjacent, adjacent)
            nonAdjacent = adjacent
            adjacent = curr
        return adjacent

obj = Solution()
#data = obj.rob(nums = [1,2,3,1])
data = obj.rob(nums = [2,7,9,3,1])
print(data)