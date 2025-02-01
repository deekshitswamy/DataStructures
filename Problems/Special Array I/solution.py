import io
from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pairty = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == pairty:
                return False
            pairty = (pairty + 1) % 2
        
        return True

obj = Solution()
#data = obj.isArraySpecial(nums = [1])
#data = obj.isArraySpecial(nums = [2,1,4])
data = obj.isArraySpecial(nums = [4,3,1,6])
print(data)