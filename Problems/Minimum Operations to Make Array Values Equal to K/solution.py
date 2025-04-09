import io
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for num in nums:
            if num > k:
                seen.add(num)
            elif num < k:
                return -1
        return len(seen)

obj = Solution()
#data = obj.minOperations(nums = [5,2,5,4,5], k = 2)
#data = obj.minOperations(nums = [2,1,2], k = 2)
data = obj.minOperations(nums = [9,7,5,3], k = 1)
print(data)