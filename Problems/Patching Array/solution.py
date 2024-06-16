import io
from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        missing = 1
        i = 0
        
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                count += 1
        
        return count

obj = Solution()
#data = obj.minPatches(nums = [1,3], n = 6)
#data = obj.minPatches(nums = [1,5,10], n = 20)
data = obj.minPatches(nums = [1,2,2], n = 5)
print(data)