import io
from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        res = 1
        for i, num in enumerate(nums):
            if num - nums[j] > k:
                res += 1
                j = i
        return res

obj = Solution()
#data = obj.partitionArray(nums = [3,6,1,2,5], k = 2)
#data = obj.partitionArray(nums = [1,2,3], k = 1)
data = obj.partitionArray(nums = [2,2,4,5], k = 0)
print(data)