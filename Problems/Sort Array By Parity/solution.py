import io
from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        return nums

obj = Solution()
#data = obj.sortArrayByParity(nums = [3,1,2,4])
data = obj.sortArrayByParity(nums = [0])
print(data)