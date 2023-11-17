import io
from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        for idx in range(n):
            ans=max(ans,nums[idx]+nums[n-idx-1])
        return ans

obj = Solution()
#data = obj.minPairSum(nums = [3,5,2,3])
data = obj.minPairSum(nums = [3,5,4,2,4,6])
print(data)