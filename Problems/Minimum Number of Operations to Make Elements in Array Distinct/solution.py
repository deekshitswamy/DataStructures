import io
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return (i + 3) // 3
            seen.add(nums[i])

        return 0

obj = Solution()
#data = obj.minimumOperations(nums = [1,2,3,4,2,3,3,5,7])
#data = obj.minimumOperations(nums = [4,5,6,4,4])
data = obj.minimumOperations(nums = [6,7,8,9])
print(data)