import io
from typing import List
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        count = l = 0
        hash = {}

        for r, num in enumerate(nums):
            hash[num] = hash.get(num, 0) + 1
            while len(hash) == total:
                count += len(nums) - r
                hash[nums[l]] -= 1
                if hash[nums[l]] == 0:
                    del hash[nums[l]]
                l += 1

        return count

obj = Solution()
#data = obj.countCompleteSubarrays(nums = [1,3,1,2,2])
data = obj.countCompleteSubarrays(nums = [5,5,5,5])
print(data)