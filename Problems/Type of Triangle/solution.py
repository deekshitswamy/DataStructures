import io
from typing import List
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

obj = Solution()
data = obj.triangleType(nums = [3,3,3])
#data = obj.triangleType(nums = [3,4,5])
print(data)