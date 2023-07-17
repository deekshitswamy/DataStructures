import io
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 > 0 :
            return False
        target = sum(nums)//2
        bit = 1
        for num in nums :
            bit = bit | bit<<num
        return bool(bit & 1<<target)

obj = Solution()
data = obj.canPartition(nums = [1,5,11,5])
#data = obj.canPartition(nums = [1,2,3,5])
print(data)