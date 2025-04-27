import io
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(nums[i]/2 == nums[i-1] + nums[i+1] for i in range(1, len(nums)-1))

obj = Solution()
#data = obj.countSubarrays(nums = [1,2,1,4,1])
data = obj.countSubarrays(nums = [1,1,1])
print(data)