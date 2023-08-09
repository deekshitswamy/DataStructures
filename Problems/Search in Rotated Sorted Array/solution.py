import io
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

obj = Solution()
#data = obj.search(nums = [4,5,6,7,0,1,2], target = 0)
#data = obj.search(nums = [4,5,6,7,0,1,2], target = 3)
data = obj.search(nums = [1], target = 0)
print(data)