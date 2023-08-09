import io
from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            k = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    k += 1
                    i += 1
                i += 1
            if k >= p:
                right = mid
            else:
                left = mid + 1
        return left

obj = Solution()
#data = obj.minimizeMax(nums = [10,1,2,7,1,3], p = 2)
data = obj.minimizeMax(nums = [4,2,1,2], p = 1)
print(data)