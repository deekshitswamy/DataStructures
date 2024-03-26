import io
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        n=len(nums)

        for i in range(1,n+1):
            if i not in nums:
                return i
        return n+1

obj = Solution()
#data = obj.firstMissingPositive(nums = [1,2,0])
#data = obj.firstMissingPositive(nums = [3,4,-1,1])
data = obj.firstMissingPositive(nums = [7,8,9,11,12])
print(data)