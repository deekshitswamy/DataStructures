import io
from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # If last elemnt is greater than first
        # Conisdeirng it as monotonically increasing
        if nums[-1]>nums[0]:
            for i in range(len(nums)-1):
                if nums[i+1]<nums[i]:
                    return False
            return True
        # Else monotonically decreasing
        else:
            for i in range(len(nums)-1):
                if nums[i+1]>nums[i]:
                    return False
            return True


obj = Solution()
#data = obj.isMonotonic(nums = [1,2,2,3])
#data = obj.isMonotonic(nums = [6,5,4,4])
data = obj.isMonotonic(nums = [1,3,2])
print(data)