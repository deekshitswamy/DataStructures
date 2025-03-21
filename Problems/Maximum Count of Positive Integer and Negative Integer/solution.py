import io
from typing import List
from bisect import bisect_left
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_neg = bisect_left(nums, 0)
        first_pos = bisect_left(nums, 1)
        neg = first_neg
        pos = len(nums) - first_pos
        return max(neg, pos)

obj = Solution()
#data = obj.maximumCount(nums = [-2,-1,-1,1,2,3])
#data = obj.maximumCount(nums = [-3,-2,-1,0,0,1,2])
data = obj.maximumCount(nums = [5,20,66,1314])
print(data)