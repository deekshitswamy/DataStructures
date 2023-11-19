import io
from typing import List
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        ans=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                ans+=i+1
        return ans

obj = Solution()
#data = obj.reductionOperations(nums = [5,1,3])
#data = obj.reductionOperations(nums = [1,1,1])
data = obj.reductionOperations(nums = [1,1,2,2,3])
print(data)