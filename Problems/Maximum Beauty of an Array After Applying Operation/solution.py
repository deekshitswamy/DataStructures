import io
from typing import List
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        left=0
        ans=0
        for i,num in enumerate(nums):
            while left<n and nums[left]<num-2*k:
                left+=1

            ans=max(ans,i-left+1)

        return ans

obj = Solution()
#data = obj.maximumBeauty(nums = [4,6,1,2], k = 2)
data = obj.maximumBeauty(nums = [1,1,1,1], k = 10)
print(data)