import io
from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = [0] * len(nums)
        totalXor = 0
        maxNum = (1 << maximumBit) - 1  # maxNum with all bits set up to maximumBit
        
        for i in range(len(nums)):
            totalXor ^= nums[i]  # Update cumulative XOR
            answer[len(nums) - i - 1] = totalXor ^ maxNum  # Calculate k and store in reverse order
            
        return answer

obj = Solution()
#data = obj.getMaximumXor(nums = [0,1,1,3], maximumBit = 2)
#data = obj.getMaximumXor(nums = [2,3,4,7], maximumBit = 3)
data = obj.getMaximumXor(nums = [0,1,2,2,5,7], maximumBit = 3)
print(data)