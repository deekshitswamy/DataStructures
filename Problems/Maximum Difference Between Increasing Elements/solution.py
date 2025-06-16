import io
from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        diff = 0
        for i in range(1,len(nums)):
            if nums[i] < mini:
                mini = nums[i]
            else:
                diff1 = nums[i] - mini
                diff = max(diff1,diff)
        if diff == 0:
            return -1
        return diff

obj = Solution()
#data = obj.maximumDifference(nums = [7,1,5,4])
#data = obj.maximumDifference(nums = [9,4,3,2])
data = obj.maximumDifference(nums = [1,5,2,10])
print(data)