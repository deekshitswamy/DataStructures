import io
from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num <= 0:
            return max_num
        return sum(set(num for num in nums if num > 0))

obj = Solution()
#data = obj.maxSum(nums = [1,2,3,4,5])
#data = obj.maxSum(nums = [1,1,0,1,1])
data = obj.maxSum(nums = [1,2,-1,-2,1,0,-1])
print(data)