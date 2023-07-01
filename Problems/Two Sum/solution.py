import io
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(0,len(nums)-1):
            m = nums[i]
            for j in range(i+1,len(nums)):
                n = nums[j]
                if m+n == target :
                    a = [i,j]

        return a

obj = Solution()
# data = obj.twoSum(nums = [2,7,11,15], target = 9)
# data = obj.twoSum(nums = [3,2,4], target = 6)
data = obj.twoSum(nums = [3,3], target = 6)
print(data)