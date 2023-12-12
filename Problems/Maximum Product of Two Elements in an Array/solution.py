import io
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)

obj = Solution()
#data = obj.maxProduct(nums = [3,4,5,2])
#data = obj.maxProduct(nums = [1,5,4,5])
data = obj.maxProduct(nums = [3,7])
print(data)