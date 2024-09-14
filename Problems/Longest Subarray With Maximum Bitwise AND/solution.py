import io
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j, max_val, res = - 1, max(nums), 0
        for i, num in enumerate(nums):
            if num != max_val: j = i
            res = max(res, i - j)
        return res

obj = Solution()
#data = obj.longestSubarray(nums = [1,2,3,3,2,2])
data = obj.longestSubarray(nums = [1,2,3,4])
print(data)