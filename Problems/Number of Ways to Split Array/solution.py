import io
from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        end, start = 0, 0
        for i in range(0, len(nums)):
            end += nums[i]
        res = 0
        for i in range(0, len(nums)-1):
            start += nums[i]
            end -= nums[i]
            if start >= end: res += 1

        return res 

obj = Solution()
#data = obj.waysToSplitArray(nums = [10,4,-8,7])
data = obj.waysToSplitArray(nums = [2,3,1,0])
print(data)